from apscheduler.schedulers.asyncio import AsyncIOScheduler
from app.services.monitor_emails import monitor_emails

scheduler = AsyncIOScheduler()

def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            monitor_emails,
            trigger="interval",
            minutes=1,
            max_instances=1,
            coalesce=True
        )
        scheduler.start()
        print("⏰ Scheduler started (Guardian email monitoring active)")
        print("To Connect Mail, Go To:http://127.0.0.1:8000/guardian/gmail/auth")

def shutdown_scheduler():
    if scheduler.running:
        scheduler.shutdown(wait=False)
        print("🛑 Scheduler stopped cleanly")
