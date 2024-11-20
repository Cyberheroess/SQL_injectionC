
import flask
from flask import request, jsonify
import mysql.connector
import html
import requests
from urllib.parse import urlparse
import ssl
import socket

app = flask.Flask(__name__)

# Fungsi untuk memeriksa HTTPS
def check_https(url):
    parsed_url = urlparse(url)
    return parsed_url.scheme == 'https'

# Fungsi untuk memeriksa header keamanan
def check_security_headers(url):
    try:
        response = requests.get(url)
        headers = response.headers
        security_headers = {
            'Strict-Transport-Security': headers.get('Strict-Transport-Security'),
            'X-Frame-Options': headers.get('X-Frame-Options'),
            'X-XSS-Protection': headers.get('X-XSS-Protection'),
            'X-Content-Type-Options': headers.get('X-Content-Type-Options'),
            'Content-Security-Policy': headers.get('Content-Security-Policy')
        }
        return security_headers
    except requests.RequestException:
        return "Tidak dapat mengakses URL"

# Fungsi untuk mendeteksi form input
def detect_input_forms(url):
    try:
        response = requests.get(url)
        if '<form' in response.text.lower():
            return "Form input terdeteksi. Perhatikan keamanan input."
        return "Tidak ada form input yang terdeteksi."
    except requests.RequestException:
        return "Tidak dapat mengakses URL"

# Fungsi bot yang diperbarui dengan Bahasa Indonesia
def bot_response(message):
    message = message.lower()
    if "halo" in message or "hai" in message:
        return "Halo! Bagaimana saya bisa membantu Anda dengan pengujian keamanan hari ini?"
    elif "sql injection" in message:
        return "Untuk menguji SQL injection, gunakan endpoint /test_sql_injection dengan permintaan POST."
    elif "xss" in message:
        return "Untuk menguji kerentanan XSS, gunakan endpoint /test_xss dengan permintaan POST."
    elif "uji website" in message:
        return "Untuk menguji sebuah website, gunakan endpoint /test_website dengan permintaan POST yang berisi URL."
    elif "bantuan" in message:
        return "Perintah yang tersedia: halo, sql injection, xss, uji website, bantuan"
    else:
        return "Maaf, saya tidak mengerti perintah tersebut. Ketik 'bantuan' untuk daftar perintah yang tersedia."

@app.route('/test_website', methods=['POST'])
def api_test_website():
    data = request.json
    url = data.get('url')
    if not url:
        return jsonify({"error": "URL tidak disediakan"}), 400
    
    results = {
        "https": check_https(url),
        "header_keamanan": check_security_headers(url),
        "form_input": detect_input_forms(url)
    }
    return jsonify(results)

@app.route('/bot', methods=['POST'])
def api_bot():
    data = request.json
    message = data.get('message', '')
    response = bot_response(message)
    return jsonify({"respons": response})

if __name__ == '__main__':
    app.run(debug=True)
