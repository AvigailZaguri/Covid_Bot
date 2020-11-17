import requests
from flask import Flask, request, Response
from config import TELEGRAM_INIT_WEBHOOK_URL, TELEGRAM_TOKEN, WEBHOOK_PORT
import bot
import message_handler

app = Flask(__name__)
requests.get(TELEGRAM_INIT_WEBHOOK_URL)


@app.route('/message', methods=["POST"])
def handle_message():
    chat_id = message_handler.extract_message_chat_id(request.get_json())
    message = bot.handle_bot(request.get_json())

    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TELEGRAM_TOKEN, chat_id,
                                                                                    message))
    return Response("success")


if __name__ == '__main__':
    app.run(port=WEBHOOK_PORT)
