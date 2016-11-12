from django.db import models


class Customer(models.Model):
    name = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField(max_length=10)
    email_id = models.EmailField()
