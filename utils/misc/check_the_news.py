from loader import db, bot
from .fetch_data import fetch_new_data
from data.config import ADMINS, STATUS_IDS

def price_format_gateway(price):
    return '{:,.2f}'.format(price)

async def send_notify_admin(message: str):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin, text=message)


async def check_lot_status():
    old_data_list = db.getAllData()
    if not old_data_list:
        return
    new_data_list = await fetch_new_data(old_data_list)
    for index in range(len(new_data_list)):
        old_data = old_data_list[index]
        new_data = new_data_list[index]
        old_status = old_data.get('lot_status')
        new_status = new_data.get('status_id')
        if old_status != new_status or new_status in [5, 7, 10, 11, 12, 16]:
            customer = new_data.get('customer_name')
            start_cost = price_format_gateway(new_data.get('start_cost'))
            new_status_text = STATUS_IDS.get(new_status)
            link = f"https://etender.uzex.uz/lot/{old_data.get('lot_id')}"
            if new_status in [5, 7, 10, 11, 12, 16]:
                file_link = f"https://apietender.uzex.uz/api/Protocol/getCancelling?id={old_data.get('lot_id')}"
                deal_cost = new_data.get('deal_cost')
                message = (f"C: {customer}\n"
                           f"Start_Cost: {start_cost}\n"
                           f"Deal_Cost: {deal_cost}\n"
                           f"Status: <b>{new_status_text}</b>\n"
                           f"<a href='{link}'>About lot</a>\n"
                           f"<a href='{file_link}'>File</a>")
                await send_notify_admin(message=message)
                db.deleteLotData(lot_id=old_data.get('lot_id'))
                continue
            message = (f"C: {customer}\n"
                       f"Start_Cost: {start_cost}\n"
                       f"Status: <b>{new_status_text}\n</b>"
                       f"<a href='{link}'>About lot</a>")
            await send_notify_admin(message=message)
            db.updateLotStatus(lot_id=old_data.get('lot_id'), lot_status=new_status)
