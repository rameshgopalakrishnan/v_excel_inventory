from django.db import models


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField()
    email_id = models.EmailField()
