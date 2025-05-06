from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = '7966826952:AAFXki6HhpWAaryvtBjVHUie4ao2R5vw-Nk'
CHAT_ID = '5813349732'

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("message", "سیگنال جدید از TradingView دریافت شد!")
    
    send_text = f"📡 سیگنال جدید:\n\n{message}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': CHAT_ID,
        'text': send_text
    }

    r = requests.post(url, json=payload)
    return "ok", 200

if __name__ == '__main__':
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port()
