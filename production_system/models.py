from django.db import models

from people.models import Customer, InternalUser
from service_and_process.models import MasterService, MasterProduct, MasterProcess


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
    """Can either be service or product"""

    service = models.ForeignKey(MasterService, null=True)
    product = models.ForeignKey(MasterProduct, null=True)
    order = models.ForeignKey(Order)
    tag_id = models.ForeignKey(MasterTag)


class MasterMaterial(models.Model):

    CHOICES = ((1, 'piece'),
               (2, 'kg'))

    label = models.TextField()
    unit = models.IntegerField(CHOICES)


class Inventory(models.Model):
    """Raw materials in purchase"""

    material = models.ForeignKey(MasterMaterial)
    quantity = models.IntegerField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField()


class Purchase(models.Model):
    """Get materials from vendor"""

    material = models.ForeignKey(MasterMaterial)
    vendor = models.TextField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()


class MappingProductMaterial(models.Model):

    product = models.ForeignKey(MasterProduct)
    material = models.ForeignKey(MasterMaterial)
    quantity = models.IntegerField()


class Task(models.Model):
    """User is ironing"""

    user = models.ForeignKey(InternalUser)
    process = models.ForeignKey(MasterProcess)
    item = models.ForeignKey(Item)
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    assigned_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()
    is_success = models.BooleanField(default=True)


class Production(models.Model):
    PRODUCTION_CHOICE = ((1, 'Training'),
                         (2, 'Actual'))

    product = models.ForeignKey(MasterProduct)
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    expected_quantity = models.IntegerField()
    output_quantity = models.IntegerField(null=True)
    type = models.IntegerField(choices=PRODUCTION_CHOICE)
    # batch


class MappingTrainerTraineeTask(models.Model):

    task_id = models.ForeignKey('production_system.Task')
    trainer = models.ForeignKey(InternalUser)
    trainee = models.ForeignKey(InternalUser)