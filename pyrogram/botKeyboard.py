from dotenv import load_dotenv,find_dotenv
import os

#Load .env variables
load_dotenv(find_dotenv())

TOKEN = os.getenv('TOKEN')
APP_ID=os.getenv('APP_ID')
APP_HASH=os.getenv('APP_HASH')
DEV = os.getenv('DEV')

#================================================

from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton,
                            ReplyKeyboardMarkup)

app = Client("my_bot")

async def main():
    async with app:
        await app.send_message(
            DEV,  # Edit this
            "This is a ReplyKeyboardMarkup example",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ["A", "B", "C", "D"],  # First row
                    ["E", "F", "G"],  # Second row
                    ["H", "I"],  # Third row
                    ["J"]  # Fourth row
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )

        await app.send_message(
            DEV,  # Edit this
            "This is a InlineKeyboardMarkup example",
            reply_markup=InlineKeyboardMarkup(
                [
                    [  # First row
                        InlineKeyboardButton(  # Generates a callback query when pressed
                            "Button",
                            callback_data="data"
                        ),
                        InlineKeyboardButton(  # Opens a web URL
                            "URL",
                            url="https://docs.pyrogram.org"
                        ),
                    ],
                    [  # Second row
                        InlineKeyboardButton(  # Opens the inline interface
                            "Choose chat",
                            switch_inline_query="pyrogram"
                        ),
                        InlineKeyboardButton(  # Opens the inline interface in the current chat
                            "Inline here",
                            switch_inline_query_current_chat="pyrogram"
                        )
                    ]
                ]
            )
        )


app.run(main())