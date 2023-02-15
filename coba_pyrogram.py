from pyrogram import Client,filters
from pyrogram import enums

# Target chat. Can also be a list of multiple chat ids/usernames
TARGET = "-1001826122574"
# Welcome message template
MESSAGE = "{} Welcome to [Pyrogram](https://docs.pyrogram.org/)'s group chat {}!"

app = Client("my_bot")

@app.on_message(filters.chat(TARGET))
async def my_handler(client,message):
    async with app:
        await app.send_message(chat_id=1908695032,text="Hi!")

    # Get members
    async for member in app.get_chat_members(chat_id=TARGET):
        print(member)

    # Get administrators
    administrators = []
    async for m in app.get_chat_members(chat_id=TARGET, filter=enums.ChatMembersFilter.ADMINISTRATORS):
        administrators.append(m)

    # Get bots
    bots = []
    async for m in app.get_chat_members(chat_id=TARGET, filter=enums.ChatMembersFilter.BOTS):
        bots.append(m)

app.run()