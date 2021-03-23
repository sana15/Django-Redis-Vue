from apscheduler.schedulers.background import BackgroundScheduler
from .update_bhavcopy_redis import sync_csvdata_from_BSE

#create background scheduler from monday to friday"

def start():
    print("starting updater")
    scheduler = BackgroundScheduler({'apscheduler.timezone': 'Asia/Calcutta'})
   
    scheduler.add_job(sync_csvdata_from_BSE, trigger='cron', day_of_week='mon-fri', hour='30', minute='17')
    
    scheduler.start()
    