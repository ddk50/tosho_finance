from apscheduler.schedulers.blocking import BlockingScheduler
from app.usecase.financial_usecase import fetch_and_save_data

scheduler = BlockingScheduler()
scheduler.add_job(fetch_and_save_data, "cron", hour=9, minute=0)

print("⏳ スケジューラーを開始しました...")
scheduler.start()
