from django.db import models
from orders.enums import AdditionalDetailsTypeEnum


class Order(models.Model):
    customer = models.ForeignKey(
        to='users.User',
        related_name='created_orders',
        on_delete=models.CASCADE
    )
    status = models.CharField(
        choices=AdditionalDetailsTypeEnum.for_choice(),
        default=AdditionalDetailsTypeEnum.CREATED,
        max_length=255
    )
    delivery_address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderProductMapping(models.Model):
    order = models.ForeignKey(
        to='orders.Order',
        related_name='ordered_products',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        to='products.Product',
        related_name='created_orders',
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField()

    class Meta:
        unique_together = ('order', 'product')
