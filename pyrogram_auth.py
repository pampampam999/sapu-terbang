from pyrogram import Client
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
APP_ID=os.getenv('APP_ID')
APP_HASH=os.getenv('APP_HASH')



print('Type of bot\n[1] User Telegram\n[2] Bot Telegram\n')
type = input("Type : ")

if type=="1":
    appName="my_accunt"
    app = Client("my_account", api_id=APP_ID, api_hash=APP_HASH)
    print("Running User Authentication | Ctrl+C to Close")
    app.run()
elif type=="2":
    app = Client(
    "my_bot",
    api_id=APP_ID, api_hash=APP_HASH,
    bot_token=TOKEN
    )
    print("Running Bot Authentication | Ctrl+C to Close")
    app.run()
else:
    print("Wrong Input")


#Use the terminal / command promnt
