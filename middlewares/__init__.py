from loader import dp
from .anti_flood import AntiFloodMiddleware
from .check_sub import CheckSubMiddleware
from .check_permit import CheckPermitMiddleware

if __name__ == "middlewares":
    dp.message.middleware(CheckPermitMiddleware())
    # dp.message.middleware(AntiFloodMiddleware())
    # dp.message.middleware(CheckSubMiddleware())
