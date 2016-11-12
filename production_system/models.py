from django.db import models

from people.models import Customer
from service_and_process.models import MasterService, MasterProduct


class Order(models.Model):

    amount = models.DecimalField(max_digits=7, decimal_places=2)
    customer_id = models.ForeignKey(Customer)
    expected_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()

    # calculate tax in the invoice

class MasterTag(models.Model):
    CHOICE = ((1, 'In Use'),
              (2, 'Free'))
    status = models.IntegerField(CHOICE)


class Item(models.Model):

    service = models.ForeignKey(MasterService)
    product = models.ForeignKey(MasterProduct)
    order = models.ForeignKey(Order)
    tag_id = models.ForeignKey(MasterTag)
