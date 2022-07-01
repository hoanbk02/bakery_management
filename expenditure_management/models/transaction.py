from django.db import models
from bakery_management.models import TrackingAbstractModel, NameAbstractModel
from .category import Category


class Transaction(TrackingAbstractModel, NameAbstractModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    note = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'{self.name} - {self.category} - {self.amount} - {self.note}'
