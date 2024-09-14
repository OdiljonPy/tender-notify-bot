from apscheduler.schedulers.asyncio import AsyncIOScheduler
from .check_the_news import check_lot_status


def run_background():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(name='Timeout reminder to members', func=check_lot_status, trigger='interval', seconds=5)
    scheduler.start()
    return
