import aiohttp
import asyncio
import ssl
import random
import argparse
import os
from colorama import Fore, Style, init


def print_banner():
    banner = """
    -----------------------------------------------------------------
                     RedOpsDB Penetration Test Team
    -----------------------------------------------------------------
    ██████╗ ███████╗██████╗  ██████╗ ██████╗ ███████╗██████╗ ██████╗ 
    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗
    ██████╔╝█████╗  ██║  ██║██║   ██║██████╔╝███████╗██║  ██║██████╔╝
    ██╔══██╗██╔══╝  ██║  ██║██║   ██║██╔═══╝ ╚════██║██║  ██║██╔══██╗
    ██║  ██║███████╗██████╔╝╚██████╔╝██║     ███████║██████╔╝██████╔╝
    ╚═╝  ╚═╝╚══════╝╚═════╝  ╚═════╝ ╚═╝     ╚══════╝╚═════╝ ╚═════╝ 
    -----------------------------------------------------------------
                 RedOpsScanner - Directory Reconnaissance
    -----------------------------------------------------------------
    """
    print(Fore.RED + banner + Style.RESET_ALL)


print_banner()
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

found_urls = []
forbidden_urls = []


def get_random_headers():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Googlebot/2.1 (+http://www.google.com/bot.html)",
    ]
    headers = {
        "User-Agent": random.choice(user_agents),
        "Referer": "https://www.google.com/",
        "Accept-Encoding": "gzip, deflate",
        "DNT": "1",
    }
    return headers


def load_wordlist(filepath):
    if not os.path.exists(filepath):
        print(f"{RED} Error: File not found {filepath}{RESET}")
        return []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except Exception as e:
        print(f"{RED}❌ Error: Cannot download file {filepath} - {e}{RESET}")
        return []


async def check_directory(session, url):
    try:
        async with session.get(url, headers=get_random_headers()) as response:
            if response.status == 200:
                print(f"{GREEN}✅ [200] FOUND: {url}{RESET}")
                found_urls.append(url)
            elif response.status == 403:
                print(f"{YELLOW}🔒 [403] FORBIDDEN: {url}{RESET}")
                forbidden_urls.append(url)
            elif response.status == 404:
                print(f"{RED}❌ [404] NOT FOUND: {url}{RESET}")
    except aiohttp.client_exceptions.ClientConnectorCertificateError:
        print(f"{RED}❌ SSL Error: Cannot connect to {url} (SSL Cert Error){RESET}")
    except Exception as e:
        print(f"{RED}⚠️ Error: {e}{RESET}")


async def main(target_url, wordlist_path, extensions):
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE  # ปิด SSL Verification

    wordlist = load_wordlist(wordlist_path)
    if not wordlist:
        print(f"{RED}Wordlist not found, empty or cannot use!{RESET}")
        return

    async with aiohttp.ClientSession(
        connector=aiohttp.TCPConnector(ssl=ssl_context)
    ) as session:
        tasks = []
        for word in wordlist:
            for ext in extensions:
                url = f"{target_url}/{word}{ext}"
                tasks.append(check_directory(session, url))
        await asyncio.gather(*tasks)

    print("\n --- Scan Summary --- ")
    print(f"{GREEN}✅ URLs Found ({len(found_urls)}):{RESET}")
    for url in found_urls:
        print(f"   {GREEN}- {url}{RESET}")

    print(f"{YELLOW}🔒 URLs Blocked (403) ({len(forbidden_urls)}):{RESET}")
    for url in forbidden_urls:
        print(f"   {YELLOW}- {url}{RESET}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Directory Scanner")
    parser.add_argument(
        "target_url", nargs="?", help="Target URL (example: https://example.com)"
    )
    parser.add_argument(
        "wordlist", nargs="?", help="Wordlist file (example: wordlist.txt)"
    )
    parser.add_argument(
        "--ext",
        nargs="+",
        default=["", ".php", ".html", ".js"],
        help="File Extension (example: .php .html)",
    )

    args = parser.parse_args()

    target_url = args.target_url or input("🔹 Input Target URL: ")
    wordlist_path = args.wordlist or input("🔹 Input Wordlist location: ")

    if not target_url or not wordlist_path:
        print(f"{RED} You MUST input Target URL and Wordlist!{RESET}")
        exit(1)

    print(f" Start scan {target_url} with Wordlist: {wordlist_path}")
    asyncio.run(main(target_url, wordlist_path, args.ext))
