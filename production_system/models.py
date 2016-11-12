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


class MasterMaterial(models.Model):

    CHOICES = ((1, 'piece'),
               (2, 'kg'))

    label = models.TextField()
    unit = models.IntegerField(CHOICES)


class Inventory(models.Model):

    material = models.ForeignKey(MasterMaterial)
    quantity = models.IntegerField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField()


class Purchase(models.Model):

    material = models.ForeignKey(MasterMaterial)
    vendor = models.TextField()
    entry_timstamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()


class MappingProductMaterial(models.Model):

    product = models.ForeignKey(MasterProduct)
    material = models.ForeignKey(MasterMaterial)
    quantity = models.IntegerField()
