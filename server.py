import requests
from flask import Flask

from config import TELEGRAM_INIT_WEBHOOK_URL

app = Flask(__name__)

requests.get(TELEGRAM_INIT_WEBHOOK_URL)

if __name__ == '__main__':
    app.run(port=5002)
