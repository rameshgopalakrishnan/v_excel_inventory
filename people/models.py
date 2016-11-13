from django.contrib.auth.models import User
from django.db import models


class MasterSection(models.Model):
    label = models.TextField(unique=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.label)


class InternalUser(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self', null=True, blank=True)
    section = models.ForeignKey(MasterSection)
    # present_trainer = models.ManyToManyField('self', through='production_system.MappingTrainerTraineeTask')

    def __str__(self):
        return "{}. {} : {}".format(self.id, self.user.username, self.section.label)


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.BigIntegerField()
    email_id = models.EmailField()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)
