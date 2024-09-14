from aiogram import Router
from aiogram.types import Message
from middlewares.check_permit import CheckPermitMiddleware

router = Router()


# Echo bot
@router.message(CheckPermitMiddleware())
async def bot_echo(message: Message):
    await message.answer(message.text)
