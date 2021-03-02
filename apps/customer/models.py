from django_extensions.db.models import TimeStampedModel

from django.db import models

__all__ = (
    'Customer'
)


class Customer(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)


class Emails(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    email_address = models.CharField(max_length=256)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


