from django.contrib.auth.models import User
from django.db import models


class CreatedAbstractModel(models.Model):
    created_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_created_by'
    )

    created_at = models.DateTimeField(
        blank=True, null=True, auto_now_add=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class ModifiedAbstractModel(models.Model):
    modified_by = models.ForeignKey(
        User,
        blank=True, null=True, on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_modified_by'
    )

    modified_at = models.DateTimeField(
        blank=True, null=True, auto_now=True,
        db_index=True,
    )

    class Meta:
        abstract = True


class TrackingAbstractModel(CreatedAbstractModel, ModifiedAbstractModel):
    class Meta:
        abstract = True


class NameAbstractModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True
