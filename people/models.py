from django.contrib.auth.models import User
from django.db import models


class MasterSection(models.Model):
     CHOICES = ((1, 'Laundry'),
                (2, 'Kitchen'))
     label = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return "{}. {}".format(self.id, self.get_label_display())


class InternalUser(models.Model):
    user = models.OneToOneField(User)
    parent = models.ForeignKey('self', null=True, blank=True)
    section = models.ForeignKey(MasterSection)
    # present_trainer = models.ManyToManyField('self', through='production_system.MappingTrainerTraineeTask')

    def __str__(self):
        return "{}. {} : {}".format(self.id, self.user.username, self.section.get_label_display())


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.BigIntegerField()
    email_id = models.EmailField()

    def __str__(self):
        return "{}. {}".format(self.id, self.name)
