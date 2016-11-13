from django.db import models

from people.models import Customer, InternalUser
from service_and_process.models import MasterService, MasterProduct, MasterProcess


class Order(models.Model):

    amount = models.DecimalField(max_digits=7, decimal_places=2)
    customer_id = models.ForeignKey(Customer)
    expected_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.id)
    # calculate tax in the invoice

    # def __str__(self):
    #     return "{}. {}".format(self.id, self.amount)

class MasterTag(models.Model):
    CHOICE = ((1, 'In Use'),
              (2, 'Free'))
    status = models.IntegerField(choices=CHOICE)

    def __str__(self):
        return "{}. {}".format(self.id, self.status)

class Item(models.Model):
    """Can either be service or product"""

    service = models.ForeignKey(MasterService, null=True)
    product = models.ForeignKey(MasterProduct, null=True)
    order = models.ForeignKey(Order)
    tag_id = models.ForeignKey(MasterTag)

    def __str__(self):
        return "{}. {}".format(self.id, self.service.label)

class MasterRawMaterial(models.Model):

    CHOICES = ((1, 'piece'),
               (2, 'kg'))

    label = models.TextField()
    unit = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return "{}. {}".format( self.id, self.label)

class Inventory(models.Model):
    """Raw materials in purchase"""

    raw_material = models.ForeignKey(MasterRawMaterial)
    quantity = models.IntegerField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField()

    def __str__(self):
        return "{}. {}".format(self.id, self.raw_material.label)

class Purchase(models.Model):
    """Get materials from vendor"""

    raw_material = models.ForeignKey(MasterRawMaterial)
    vendor = models.TextField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}. {}. {}".format(self.id, self.raw_material.label, self.vendor)

class MappingProductMaterial(models.Model):

    product = models.ForeignKey(MasterProduct)
    raw_material = models.ForeignKey(MasterRawMaterial)
    quantity = models.IntegerField()

    def __str__(self):
        return "{}. {}".format(self.id, self.product.label)

class Task(models.Model):
    """User is ironing"""

    user = models.ForeignKey(InternalUser)
    process = models.ForeignKey(MasterProcess)
    item = models.ForeignKey(Item)
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    assigned_timestamp = models.DateTimeField()
    completed_timestamp = models.DateTimeField()
    is_success = models.BooleanField(default=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.user.user.username)

class Production(models.Model):
    PRODUCTION_CHOICE = ((1, 'Training'),
                         (2, 'Actual'))

    item = models.ForeignKey(Item)
    product = models.ForeignKey(MasterProduct)
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    expected_quantity = models.IntegerField()
    output_quantity = models.IntegerField(null=True)
    production_type = models.IntegerField(choices=PRODUCTION_CHOICE)
    # batch

    def __str__(self):
        return "{}. {}".format(self.id, self.production_type)

class ProductInventory(models.Model):
    """Holds the current state of the product (cookies, chocolates) Inventory"""
    product = models.ForeignKey(MasterProduct)
    quantity = models.IntegerField()
    entry_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField()

    def __str__(self):
        return "{}. {}".format(self.id, self.product.label)

class MappingTrainerTraineeTask(models.Model):

    task_id = models.ForeignKey('production_system.Task')
    trainer = models.ForeignKey(InternalUser, related_name='trainer')
    trainee = models.ForeignKey(InternalUser, related_name='trainee')
