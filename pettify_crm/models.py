from django.db import models
from model_utils.models import TimeStampedModel, StatusModel, SoftDeletableModel
from model_utils import Choices


class Address(TimeStampedModel, SoftDeletableModel):
    class Meta:
        db_table = 'address'
    address = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150, blank=True)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True)


class Animal(StatusModel, SoftDeletableModel):
    class Meta:
        abstract = True
    STATUS = Choices('unavailable', 'available', 'adopted')
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Cat(Animal):
    class Meta:
        db_table = 'cat'
    pass
