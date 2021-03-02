from django_extensions.db.models import TimeStampedModel

from django.db import models
from django.db.models import Case, Value, When, F, Func
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.aggregates import ArrayAgg


class AbstractProduct(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    product_name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        abstract = True


class CustomProduct(AbstractProduct):
    pass


class NonCustomProduct(AbstractProduct):
    pass


class Order(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    order_number = models.CharField(max_length=256)

    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE)
    status = models.ForeignKey('order.OrderStatus', on_delete=models.CASCADE)

    @classmethod
    def get_paid_orders(cls):
        orders = (
            cls.objects.filter(status__paid=True).prefetch_related('customer', 'orderitem')
            .annotate(
                products=ArrayAgg(
                    Case(
                        When(orderitem__product=None, then=Func(
                            Value('product_price'), 'orderitem__np__price',
                            Value('product_name'), 'orderitem__np__product_name',
                            function='jsonb_build_object'
                        )),
                        When(orderitem__np=None, then=Func(
                            Value('product_price'), 'orderitem__product__price',
                            Value('product_name'), 'orderitem__product__product_name',
                            function='jsonb_build_object'
                        )),
                        output_field=JSONField(),
                    )
                )
            )
            .values(
                'products',
                'order_number',
                first_name=F('customer__first_name'),
                last_name=F('customer__last_name'),
                email_address=F('customer__emails__email_address'),
            )
        )
        return orders


class OrderStatus(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    paid = models.BooleanField(default=False)


class OrderItem(TimeStampedModel):
    id = models.BigAutoField(unique=True, primary_key=True)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('order.CustomProduct', null=True, on_delete=models.CASCADE)
    np = models.ForeignKey('order.NonCustomProduct', null=True, on_delete=models.CASCADE)
