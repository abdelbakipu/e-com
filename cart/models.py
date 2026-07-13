from django.db import models

# Create your models here.

class Cart(models.Model):
    user = models.OneToOneField('accounts.CustomUser', on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} cart!"
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='items')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"#{self.cart.id}: {self.product.name} x {self.quantity}"