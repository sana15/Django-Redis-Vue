from django.apps import AppConfig
import logging


class SyncConfig(AppConfig):
    name = 'sync'
    def ready(self):
        from . import updater
        updater.start()
