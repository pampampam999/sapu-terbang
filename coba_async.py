import asyncio
from telebot.async_telebot import AsyncTeleBot
import os
import aiohttp

#bot identity
TOKEN = os.getenv('TOKEN')
bot = AsyncTeleBot(TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    await bot.send_message(-1001826122574, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.send_message(-1001826122574, message.text)


asyncio.run(bot.polling())