from bakery_management.models import TrackingAbstractModel, NameAbstractModel


class Category(TrackingAbstractModel, NameAbstractModel):

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'
