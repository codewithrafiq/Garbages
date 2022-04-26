from django.db import models



class BaseModel(models.Model):
    """
    BaseModel class is a parent class for all models.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=True)

    class Meta:
        abstract = True