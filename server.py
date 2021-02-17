import requests
from flask import Flask, request, Response
from config import TELEGRAM_INIT_WEBHOOK_URL, TELEGRAM_TOKEN, WEBHOOK_PORT
import bot
import message_handler

app = Flask(__name__)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    message = request.get_json()["message"]
    chat_id = message['chat']['id']
    note = bot.handle_bot(message)
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TELEGRAM_TOKEN, chat_id,
                                                                                        note))
    return Response("success")


if __name__ == '__main__':
    app.run(port=WEBHOOK_PORT)
