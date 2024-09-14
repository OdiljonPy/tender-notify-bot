import asyncio
import middlewares
from loader import dp, bot, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from utils.misc.apscheduler import run_background
from handlers.users.routes import user_router


async def on_startup():
    # Create db sqlite
    db.create_table_lot()

    # Birlamchi komandalar (/star va /help)
    await set_default_commands()

    # Bot ishga tushgani haqida adminga xabar berish
    await on_startup_notify(bot)

    # Create background task
    run_background()

    # Include user routers
    dp.include_router(user_router)
    await bot.delete_webhook(drop_pending_updates=True)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(on_startup())
    # executor.start_polling(dp, on_startup=on_startup)
