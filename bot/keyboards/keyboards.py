# bot/keyboards/keyboards.py

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_link_content():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Доступ", style="primary", url="https://t.me/aokigahara11")]
        ]
    )