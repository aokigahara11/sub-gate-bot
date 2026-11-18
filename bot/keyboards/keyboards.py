# bot/keyboards/keyboards.py

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from bot.config.config import ACCESS_URL


def get_link_content():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Доступ", style="primary", url=ACCESS_URL)]
        ]
    )