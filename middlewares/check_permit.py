from aiogram.types import Message, CallbackQuery
from aiogram import BaseMiddleware
from typing import Any, Callable, Dict, Awaitable, Union
from data.config import ADMINS


class CheckPermitMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Union[Message, CallbackQuery],
            data: Dict[str, Any]
    ) -> Any:
        if isinstance(event, CallbackQuery):
            user_id = event.message.from_user.id
            if not user_id in ADMINS:
                await event.message.answer(
                    text="У вас нет разрешения на использование бота!"
                )
                return
        if isinstance(event, Message):
            user_id = event.from_user.id
            if not user_id in ADMINS:
                await event.answer(
                    text="У вас нет разрешения на использование бота!"
                )
                return
        return await handler(event, data)
