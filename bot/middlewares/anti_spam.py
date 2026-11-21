from collections.abc import Awaitable, Callable
from time import monotonic
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message
from aiogram.types.base import TelegramObject


class AntiSpamMiddleware(BaseMiddleware):
    def __init__(self, rate_limit: float = 1.0) -> None:
        if rate_limit <= 0:
            raise ValueError("rate_limit must be greater than zero")

        self.rate_limit = rate_limit
        self._last_event_at: dict[int, float] = {}

    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        if isinstance(event, CallbackQuery):
            user_id = event.from_user.id
        elif isinstance(event, Message) and event.from_user is not None:
            user_id = event.from_user.id
        else:
            return await handler(event, data)

        now = monotonic()
        last_event_at = self._last_event_at.get(user_id)

        if last_event_at is not None and now - last_event_at < self.rate_limit:
            if isinstance(event, CallbackQuery):
                await event.answer("Не так быстро!")
            return None

        self._last_event_at[user_id] = now
        return await handler(event, data)
