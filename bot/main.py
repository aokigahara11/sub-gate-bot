# bot/main.py
import asyncio
import sys
from pathlib import Path

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from aiogram import Bot, Dispatcher, types

from utils.logger import logger
from bot.config.config import TELEGRAM_TOKEN_BOT
from bot.handlers import router as handlers_router
from bot.middlewares import AntiSpamMiddleware

async def set_bot_commands(Bot: Bot):
    commands = [
        types.BotCommand(command='start', description='Начать'),
        types.BotCommand(command='stats', description='Статистика')
    ]
    await Bot.set_my_commands(commands)

bot = Bot(token=TELEGRAM_TOKEN_BOT)
dp = Dispatcher()

dp.message.outer_middleware(AntiSpamMiddleware(rate_limit=1.0))
dp.callback_query.outer_middleware(AntiSpamMiddleware(rate_limit=1.0))
dp.include_router(handlers_router)

async def main():
    await set_bot_commands(bot)
    logger.info("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

