from pyrogram import Client
from dotenv import load_dotenv,find_dotenv
import os

TOKEN = os.getenv('TOKEN')
APP_ID=os.getenv('APP_ID')
APP_HASH=os.getenv('APP_HASH')

app = Client(
    "my_bot",
    api_id=APP_ID, api_hash=APP_HASH,
    bot_token=TOKEN
)
print("Running Bot Authentication")
app.run()