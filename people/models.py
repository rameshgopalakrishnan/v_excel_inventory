from django.contrib.auth.models import User
from django.db import models

from service_and_process.models import MasterProcess


class MasterUnit(models.Model):
    CHOICES = ((1, 'Laundry'),
               (2, 'Kitchen'))
    label = models.IntegerField(CHOICES)


class InternalUser(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self')
    unit = models.ForeignKey(MasterUnit)


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField()
    email_id = models.EmailField()


class MappingUserProcess(models.Model):
    """User is ironing"""

    user = models.ForeignKey(User)
    process = models.ForeignKey(MasterProcess)
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    assigned_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()
    is_success = models.BooleanField(default=True)
