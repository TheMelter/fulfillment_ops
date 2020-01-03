from django.db import models
from django.utils.timezone import now
from . import OrderStatus, OrderEvents
from ..product.models import ProductVariant


class Order(models.Model):
    created = models.DateTimeField(default=now, editable=False)
    status = models.CharField(
        max_length=32, default=OrderStatus.CREATED, choices=OrderStatus.CHOICES
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=4
    )


class OrderLine(models.Model):
    order = models.ForeignKey(
        Order, related_name="lines", editable=False, on_delete=models.CASCADE
    )
    variant = models.ForeignKey(
        ProductVariant,
        related_name="order_lines",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=4
    )


class OrderEvent(models.Model):
    date = models.DateTimeField(default=now, editable=False)
    type = models.CharField(
        max_length=255,
        choices=OrderEvents.CHOICES,
    )
    order = models.ForeignKey(Order, related_name="events", on_delete=models.CASCADE)

