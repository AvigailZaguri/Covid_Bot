import pymysql


# config bot
WEBHOOK_PORT = 5002
TELEGRAM_TOKEN ='1217952102:AAHiIKy8gXqS-1ypbPxRamOadGDdBOxyQxY'
WEBHOOK_URL = 'https://2d07ade601b0.ngrok.io'
TELEGRAM_INIT_WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook?url={}/message'.format(TELEGRAM_TOKEN,
                                                                                              WEBHOOK_URL)


# config database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="Az97185Az!",
    db="coivdbotdb",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)

if connection.open:
    print("the connection is opened")
