from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
import os


# @receiver(pre_save, sender=User)
# def create_user_profile(sender, instance, **kwargs):
#         try:
#             try:
#                 os.makedirs('users_databases')
#             except Exception as e:
#                 pass
#             f = open(f'./users_databases/{instance.username}.db','w')
#             f.close()
#         except Exception as e:
#             print(e)


# @receiver(post_save, sender=User)
# def user_create(sender, instance, created, **kwargs):
#     if created:
#             os.system('python3 manage.py migrate_all_db')


class Todo(models.Model):
    user = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class TestTable(models.Model):
    title = models.CharField(max_length=10,blank=True, null=True)