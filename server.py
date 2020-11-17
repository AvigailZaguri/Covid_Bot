import requests
from flask import Flask, request, Response

from config import TELEGRAM_INIT_WEBHOOK_URL, TELEGRAM_TOKEN

app = Flask(__name__)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    chat_id = request.get_json()['message']['chat']['id']
    message = request.get_json()["message"]
    user_name = message['from']['id']
    print(user_name)
    message = request.get_json()['message']['text']
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TELEGRAM_TOKEN, chat_id,
                                                                                        "I love you"))

    return Response("success")


if __name__ == '__main__':
    app.run(port=5002)
