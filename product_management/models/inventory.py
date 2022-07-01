from django.db import models
from bakery_management.models import TrackingAbstractModel
from product_management.constants import QuantityType
from .product import Product


class History(TrackingAbstractModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    action = models.IntegerField(default=QuantityType.NEW, choices=QuantityType.QUANTITY_TYPE_CHOICES)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Histories'

    def __str__(self):
        return f'{self.product.name} - {self.price}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.price = self.product.price
        super(History, self).save(force_insert, force_update, using, update_fields)
        if self.action == QuantityType.NEW:
            self.product.quantity += self.quantity
        elif self.action == QuantityType.EXPIRED:
            if self.product.quantity < self.quantity:
                raise ValueError(
                    "Cannot update history because current_quantity < expired_quantity."
                )
            self.product.quantity -= self.quantity
        else:
            if self.product.quantity < self.quantity:
                raise ValueError("Cannot update history because product_quantity < quantity.")
            self.product.quantity = self.quantity
        self.product.save()
