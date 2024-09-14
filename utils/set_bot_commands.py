from aiogram.types import BotCommand, BotCommandScopeDefault
from loader import bot


async def set_default_commands():
    commands = [
        BotCommand(
            command="start",
            description="Запустить бота."
        ),
        BotCommand(
            command="help",
            description="Помощь."
        ),
        BotCommand(
            command="add_lot",
            description="Добавить новый лот"
        )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
