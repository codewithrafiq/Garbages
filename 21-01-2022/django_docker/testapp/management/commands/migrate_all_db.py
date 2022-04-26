
from common_utiles.decorator import SwitchDatabase
from django.db import connections
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import logging
from django.core.management import call_command


logger = logging.getLogger(__name__)
class Command(BaseCommand):
    def handle(self, *args, **options):
        dbs = User.objects.all()
        for db in dbs:
            logger.info("Applying Migrations to database: %s", db.username)
            logger.info("======================================================")
            print("Applying Migrations to database: {}".format(db.username))
            print("======================================================")
            SwitchDatabase.switch(db.username)
            cursor = connections[db.username].cursor()
            call_command('migrate', '--database=' + db.username)
            cursor.close()