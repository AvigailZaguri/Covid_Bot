import pymysql


# config bot
WEBHOOK_PORT = 5002
TELEGRAM_TOKEN ='1438436987:AAG5n5E1h9sXKeoT7zrbcWOBO__dkvuqfCg'
WEBHOOK_URL = 'https://e6246e86f80c.ngrok.io'
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
