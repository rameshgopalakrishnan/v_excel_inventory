from django.contrib.auth.models import User
from django.db import models

from service_and_process.models import MasterProcess


class MasterSection(models.Model):
    CHOICES = ((1, 'Laundry'),
               (2, 'Kitchen'))
    label = models.IntegerField(CHOICES)


class InternalUser(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self')
    section = models.ForeignKey(MasterSection)
    present_trainer = models.ManyToManyField('self', through='production_system.MappingTrainerTraineeTask')


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField()
    email_id = models.EmailField()
