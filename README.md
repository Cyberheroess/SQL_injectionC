## sql_injection
## Instalasi
1. Pastikan Python 3.7+ terinstal di sistem Anda.
2. Install dependensi yang diperlukan:
   ```
   pip install flask mysql-connector-python requests
   ```
3. Unduh file `security_test_bot.py` ke direktori kerja Anda.

## Penggunaan Bot
Untuk menjalankan bot:
1. Buka terminal atau command prompt.
2. Navigasi ke direktori tempat `security_test_bot.py` berada.
3. Jalankan perintah:
   ```
   python security_test_bot.py
   ```
4. Server akan berjalan di `http://localhost:5000`.

## Endpoint API

### 1. /bot
- Metode: POST
- Deskripsi: Berinteraksi dengan bot untuk mendapatkan informasi.
- Body request:
  ```json
  {
    "message": "pesan Anda di sini"
  }
  ```

### 2. /test_website
- Metode: POST
- Deskripsi: Melakukan pengujian keamanan dasar pada website.
- Body request:
  ```json
  {
    "url": "https://contoh.com"
  }
  ```

### 3. /test_sql_injection
- Metode: POST
- Deskripsi: Melakukan pengujian SQL Injection.
- Body request:
  ```json
  {
    "query": "SELECT * FROM users WHERE id = %s",
    "params": [1]
  }
  ```

### 4. /test_xss
- Metode: POST
- Deskripsi: Melakukan pengujian Cross-Site Scripting (XSS).
- Body request:
  ```json
  {
    "input": "<script>alert('XSS')</script>"
  }
  ```

## Contoh Penggunaan

### Menggunakan Bot
```bash
curl -X POST http://localhost:5000/bot -H "Content-Type: application/json" -d '{"message": "halo"}'
```

### Menguji Website
```bash
curl -X POST http://localhost:5000/test_website -H "Content-Type: application/json" -d '{"url": "https://ngajilagi.id"}'
```

### Menguji SQL Injection
```bash
curl -X POST http://localhost:5000/test_sql_injection -H "Content-Type: application/json" -d '{"query": "SELECT * FROM users WHERE id = %s", "params": [1]}'
```

### Menguji XSS
```bash
curl -X POST http://localhost:5000/test_xss -H "Content-Type: application/json" -d '{"input": "<script>alert('XSS')</script>"}'
```
