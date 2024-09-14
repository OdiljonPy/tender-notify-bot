from aiogram import types, Router, F
from loader import db
from utils.misc.fetch_data import fetch_new_data

router = Router()


@router.message(F.text.startswith('/add_lot'))
async def create_new_lot(message: types.Message):
    lot_id = str(message.text.split()[1]).strip()
    if not lot_id.isdigit():
        await message.answer(
            text='Идентификатор лота должен быть числом!'
        )
        return
    if db.getLotData(lot_id=lot_id):
        await message.answer(
            text="Эта информация уже доступна!"
        )
        return
    result = await fetch_new_data(int(lot_id))
    if result[0].get('status') and result[0].get('status') >= 400:
        await message.answer(
            text="Идентификатор ошибочного лота",
            reply_to_message_id=message.message_id
        )
        return
    status = result[0].get('status_id')
    db.addLotData(lot_id=lot_id, lot_status=status)
    await message.answer(
        text="Идентификатор лота добавлен.",
        reply_to_message_id=message.message_id
    )
