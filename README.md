# RedOpsScanner - Directory Reconnaissance Tool
![22RedOps](https://github.com/user-attachments/assets/1219966a-c88f-46dd-aa05-1408310a7083)<br><br>
RedOpsScanner is a tool for scanning hidden directories and files on a web server. It utilizes `aiohttp` and `asyncio` for efficient scanning. Users can specify a custom wordlist and file extensions to scan for. The tool supports asynchronous execution, making the scanning process much faster.

## Key Features
- Accepts URL, wordlist, and file extensions from users<br>
- Interactive input support (if no arguments are provided)<br>
- Asynchronous execution (asyncio + aiohttp) for high-speed directory scanning<br>
- Parallel directory testing to maximize efficiency<br>
- Customizable file extensions (e.g., .php, .html, .js)<br>
- Randomized User-Agent for evading bot detection<br>
- Uses Google Referer to mimic real traffic and reduce blocking risks<br>
- Bypasses SSL verification to scan HTTPS sites with certificate issues<br>
- Handles HTTP response codes: ✅ 200 (Found) ✅ 403 (Forbidden) ✅ 404 (Not Found)<br>
- Handles SSL errors and connection failures gracefully<br>
- Color-coded terminal output for better readability<br>
- Supports external wordlists for directory and file discovery<br>
- Detects web restrictions (403 Forbidden responses)<br>
- Generates a scan summary report at the end<br>
- Error handling for invalid URLs and unreachable servers<br>
- Retries failed requests when encountering temporary errors<br>
- Detects redirections and follows them if necessary<br>
- Handles directory traversal errors (e.g., invalid characters in URLs)<br>
- Customizable request headers to simulate different client behavior<br>
- Safe execution with exception handling to avoid crashes<br>
- CLI-based execution for automation and scripting<br>

## Installation
1. Install `Python 3.7+`
2. Install the required libraries:
   ```sh
   pip install aiohttp colorama
   ```

## 🚀 Usage
### Basic Command
```sh
python redopsscanner.py <target_url> <wordlist_path> --ext .php .html .js
```
### Example Usage
```sh
python redopsscanner.py https://example.com wordlist.txt --ext .php .html .js
```
Alternatively, you can enter values interactively:
```sh
python redopsscanner.py
🔹 Input Target URL: https://example.com
🔹 Input Wordlist location: wordlist.txt
```

## Output Explanation
- ✅ **[200] FOUND**: Directory or file exists
- 🔒 **[403] FORBIDDEN**: Exists but access is restricted
- ❌ **[404] NOT FOUND**: Does not exist

## 📋 Example Output
```
Start scan https://example.com with Wordlist: wordlist.txt
✅ [200] FOUND: https://example.com/admin
🔒 [403] FORBIDDEN: https://example.com/secret
❌ [404] NOT FOUND: https://example.com/notexist

--- Scan Summary ---
✅ URLs Found (1):
   - https://example.com/admin
🔒 URLs Blocked (403) (1):
   - https://example.com/secret
```

## Disclaimer
- Do not use this tool on websites without proper authorization. Unauthorized use may be illegal.
- This tool is intended for educational and penetration testing purposes only.<br><br><br>

# RedOpsScanner - Directory Reconnaissance Tool
RedOpsScanner เป็นเครื่องมือสำหรับสแกนหา Directory และไฟล์ที่ซ่อนอยู่บนเว็บเซิร์ฟเวอร์ โดยใช้ `aiohttp` และ `asyncio` เพื่อเพิ่มประสิทธิภาพในการสแกน สามารถกำหนด Wordlist และนามสกุลของไฟล์ที่ต้องการค้นหาได้ รองรับการทำงานแบบ Asynchronous ทำให้สามารถสแกนได้อย่างรวดเร็ว
## คุณสมบัติ
- รองรับการป้อน URL, Wordlist และส่วนขยายไฟล์ จากผู้ใช้<br>
- รองรับการป้อนค่าแบบโต้ตอบ (หากไม่มีการระบุพารามิเตอร์)<br>
- ใช้การประมวลผลแบบอะซิงโครนัส (asyncio + aiohttp) เพื่อสแกนไดเรกทอรีความเร็วสูง<br>
- สามารถสแกนหลายไดเรกทอรีพร้อมกัน เพื่อเพิ่มประสิทธิภาพ<br>
- กำหนดนามสกุลไฟล์เองได้ (เช่น .php, .html, .js)<br>
- สุ่ม User-Agent เพื่อลดโอกาสถูกตรวจจับจากระบบป้องกันบอท<br>
- ใช้ Referer ของ Google เพื่อเลียนแบบทราฟฟิกจริง ลดโอกาสถูกบล็อก<br>
- สามารถปิดการตรวจสอบ SSL เพื่อสแกนเว็บไซต์ HTTPS ที่มีปัญหาใบรับรอง<br>
- ตรวจจับรหัสสถานะ HTTP ได้อย่างแม่นยำ: ✅ 200 (พบ) ✅ 403 (ถูกบล็อก) ✅ 404 (ไม่พบ)<br>
- จัดการข้อผิดพลาด SSL และปัญหาการเชื่อมต่อได้อย่างเหมาะสม<br>
- รองรับ Wordlist ภายนอก เพื่อค้นหาไดเรกทอรีและไฟล์ที่ซ่อนอยู่<br>
- ตรวจจับข้อจำกัดของเว็บเซิร์ฟเวอร์ (403 Forbidden)<br>
- สร้างรายงานสรุปผลการสแกน เมื่อสแกนเสร็จสิ้น<br>
- จัดการข้อผิดพลาด URL ไม่ถูกต้อง และเซิร์ฟเวอร์ที่ไม่สามารถเข้าถึงได้<br>
- ลองส่งคำขอใหม่ (Retry) เมื่อเจอข้อผิดพลาดชั่วคราว<br>
- ตรวจจับการ Redirect และตามลิงก์ไปยังเป้าหมายหากจำเป็น<br>
- รองรับการจัดการข้อผิดพลาดของ Directory Traversal (เช่น ตัวอักษรที่ไม่ถูกต้องใน URL)<br>
- รองรับการกำหนด Header เอง เพื่อจำลองพฤติกรรมของไคลเอนต์ที่แตกต่างกัน<br>
- ป้องกันการเกิดข้อผิดพลาดร้ายแรง (Exception Handling) เพื่อให้โปรแกรมไม่หยุดทำงาน<br>
- รองรับการใช้งานผ่าน CLI ทำให้สามารถใช้งานร่วมกับสคริปต์และระบบอัตโนมัติได้<br>

## วิธีติดตั้ง
1. ติดตั้ง `Python 3.7+`
2. ติดตั้งไลบรารีที่จำเป็น:
   ```sh
   pip install aiohttp colorama
   ```

## วิธีใช้งาน
### คำสั่งพื้นฐาน
```sh
python redopsscanner.py <target_url> <wordlist_path> --ext .php .html .js
```
### ตัวอย่างการใช้งาน
```sh
python redopsscanner.py https://example.com wordlist.txt --ext .php .html .js
```
หรือหากต้องการป้อนค่าภายหลัง:
```sh
python redopsscanner.py
🔹 Input Target URL: https://example.com
🔹 Input Wordlist location: wordlist.txt
```

## รายละเอียดการแสดงผล
- ✅ **[200] FOUND**: Directory or file exists
- 🔒 **[403] FORBIDDEN**: Exists but access is restricted
- ❌ **[404] NOT FOUND**: Does not exist

## ตัวอย่างผลลัพธ์
```
Start scan https://example.com with Wordlist: wordlist.txt
✅ [200] FOUND: https://example.com/admin
🔒 [403] FORBIDDEN: https://example.com/secret
❌ [404] NOT FOUND: https://example.com/notexist

--- Scan Summary ---
✅ URLs Found (1):
   - https://example.com/admin
🔒 URLs Blocked (403) (1):
   - https://example.com/secret
```

## !! คำเตือน !!
- ห้ามใช้เครื่องมือนี้กับเว็บไซต์ที่ไม่ได้รับอนุญาต การใช้งานโดยไม่ได้รับอนุญาตอาจผิดกฎหมาย
- ใช้เพื่อการศึกษาและทดสอบด้าน PenTest เท่านั้น<br><br><br>
