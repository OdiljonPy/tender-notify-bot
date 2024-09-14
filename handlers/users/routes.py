from aiogram import Router
from . import start
from . import help
from . import echo
from . import add_lot

user_router = Router()
user_router.include_routers(
    *[
        start.router,
        help.router,
        add_lot.router,
        echo.router,
    ]
)
