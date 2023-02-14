from pyrogram import Client
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
APP_ID=os.getenv('APP_ID')
APP_HASH=os.getenv('APP_HASH')

app = Client("my_account", api_id=APP_ID, api_hash=APP_HASH)

print("Running User Authentication")
app.run()

#Use the terminal / command promnt
