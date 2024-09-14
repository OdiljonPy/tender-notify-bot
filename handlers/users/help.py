from aiogram import types, Router
from aiogram.filters import Command

router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    text = ("Команды: ",
            "/start - Запустить бота",
            "/help - Помощь",
            "/add_lot - Добавить новый лот")
    await message.answer("\n".join(text))
