from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Order(models.Model):
    class Status(models.TextChoices):
        # pending/paid/shipped/delivered/cancelled
        PENDING = 'PE', _('Pending Approval')
        PAID = 'PA', _('Paid')
        SHIPPED = 'SH', _('Shipped out')
        DELIVERED = 'DE', _('Delivered to Customer')
        CANCELLED = 'CA', _('Cancelled') 


    user = models.ForeignKey('accounts.CustomUser', on_delete=models.PROTECT, related_name='orders')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.PENDING)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    shipping_address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.SET_NULL, related_name='orders', null=True)
    quantity = models.PositiveIntegerField()
    price_at_purchase = models.DecimalField(max_digits=6, decimal_places=2)
