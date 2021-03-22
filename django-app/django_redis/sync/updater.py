from apscheduler.schedulers.background import BackgroundScheduler
from .something_update import update_something



def start():
    print("starting updater")
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Calcutta'})
    # scheduler.add_job(update_bhavcopy_redis, 'interval', seconds=100)
    scheduler.add_job(update_bhavcopy_redis, trigger='cron', day_of_week='mon-fri', hour='18', minute='03')
    
    scheduler.start()
    