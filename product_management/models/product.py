from django.db import models
from bakery_management.models import TrackingAbstractModel, NameAbstractModel


class Product(TrackingAbstractModel, NameAbstractModel):
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Products'

    def __str__(self):
        return f'{self.name} - {self.price} - {self.quantity}'
