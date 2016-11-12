from django.db import models


class MasterWorkable(models.Model):
    """e.g. Shirt, T. Shirt, Trousers"""

    CATEGORY_CHOICES = ((1, 'Gentlemen'),
                        (2, 'Women'))

    label = models.TextField()
    category = models.IntegerField(choices=CATEGORY_CHOICES)


class MasterService(models.Model):
    """e.g. Dry Washing"""

    label = models.TextField()
    workable = models.ForeignKey(MasterWorkable)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)


class MasterProcess(models.Model):
    """e.g. Billing, Sorting, QC, Washing"""

    label = models.TextField()
    models.ManyToManyField(MasterService)
