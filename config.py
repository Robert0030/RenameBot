import os
import re

id_pattern = re.compile(r'^.\d+$')
# get a token from @BotFather
TOKEN = os.environ.get("TOKEN", "")
# The Telegram API things
APP_ID = int(os.environ.get("APP_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
#Array to store users who are authorized to use the bot
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
#Your Mongo DB Database Name
DB_NAME = os.environ.get("DB_NAME", "my")
#Your Mongo DB URL Obtained From mongodb.com
DB_URL = os.environ.get("DB_URL", "")

START_PIC = os.environ.get("START_PIC", "")

PORT = os.environ.get("PORT", "8080")

FORCE_SUB = os.environ.get("FORCE_SUB", "")

FLOOD = int(os.environ.get("FLOOD", "5"))
