from django.contrib.auth.models import User
from django.db import models


class MasterSection(models.Model):
    CHOICE = ((1, 'Laundry'),
              (2, 'Kitchen'))
    label = models.IntegerField(choices=CHOICE)

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

<<<<<<< HEAD
    def __str__(self):
        return "{}. {}".format(self.id, self.name)
=======
class Service(models.Model):
    label = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
>>>>>>> 2fd178031bbaf4f8bf86d0ee9049ecbd9b0580ad
