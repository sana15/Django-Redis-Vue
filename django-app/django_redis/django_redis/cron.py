from django_cron import CronJobBase, Schedule
from django.core.management.base import BaseCommand, CommandError
import os
from crontab import CronTab
# class MyCronJob(CronJobBase):
#     RUN_EVERY_MINS = 1 # every 2 hours

#     schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#     code = 'my_app.my_cron_job'    # a unique code

# def do(self):
#         # do your thing here
#     print("print every minute")

def my_scheduled_job():
  print("okay")
  with open("test.txt","w") as file:
      file.write("something")