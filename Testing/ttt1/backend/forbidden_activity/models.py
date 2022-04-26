from utils.base_model_class import BaseModelClass
from django.db import models


class Activity(BaseModelClass):
    title = models.CharField(max_length=100)


class Department(BaseModelClass):
    title = models.CharField(max_length=100)


class Line(BaseModelClass):
    title = models.CharField(max_length=100)
    total_worker = models.IntegerField(blank=True,null=True)


class Floor(BaseModelClass):
    title = models.CharField(max_length=100)
    total_worker = models.IntegerField(blank=True,null=True)


class Worker(BaseModelClass):
    name = models.CharField(max_length=100)
    image = models.URLField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    floor = models.ForeignKey(Floor, on_delete=models.CASCADE)


class ForbiddenActivity(BaseModelClass):
    worker = models.ForeignKey(
        Worker, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    worker_uuid = models.IntegerField(blank=True, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    total_time = models.IntegerField()
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)


class Entry(BaseModelClass):
    worker = models.ForeignKey(
        Worker, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    time = models.DateTimeField()
    person = models.IntegerField()


class Exit(BaseModelClass):
    worker = models.ForeignKey(
        Worker, on_delete=models.SET_NULL, blank=True, null=True, default=None)
    time = models.DateTimeField()
    person = models.IntegerField()
