# bot/handlers/start.py
from aiogram.filters import CommandStart
from aiogram import Router, types

from bot.api.subgram_api import SubgramAPI
from utils.logger import logger
from bot.keyboards.keyboards import get_link_content

router = Router()

@router.message(CommandStart)
async def start_cmd(message: types.Message):
    """Обработчик команды старт"""
    msg = "Задания выполены! Получить доступ к сериалу по кнопке ниже"
    
    await message.answer(
        msg,
        reply_markup=get_link_content(),
        parse_mode="HTML"
    )


