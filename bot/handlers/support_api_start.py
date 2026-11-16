# bot/handlers/start.py
from aiogram.filters import CommandStart
from aiogram import Router, types

from bot.api.subgram_api import subgram_api
from utils.logger import logger
from bot.keyboards.keyboards import get_link_content

router = Router()

@router.message(CommandStart)
async def start_cmd(message: types.Message):
    """Обработчик команды старт"""
    response = await subgram_api.get_tasks(
        api_key=subgram_api.api_key,
        user_id=message.from_user.id,
        chat_id=message.chat.id
    )
    
    logger.info(f"Запрос SUBGRAM: {response} ")

    if response:
        status = response.get("status")

        if status == "warning":
            # Warning - тип статуса, если пользователь не подписан
            # Сервис предложит подписки самостоятельно
            return 

        if status == "error":
            logger.error(f"Ошибка SubgramAPI: {response.get('message')}")
            return

    msg = "Задания выполены! Получить доступ к сериалу по кнопке ниже"

    await message.answer(
        msg,
        reply_markup=get_link_content(),
        parse_mode="HTML"
    )


