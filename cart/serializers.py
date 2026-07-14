from rest_framework import serializers
from accounts.serializer import UserProfileSerializer
from products.serializers import ProductListSerializer
from products.models import Product
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductListSerializer(source = 'product', read_only = True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = CartItem
        fields = ['product','product_detail', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many = True, read_only = True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['items', 'total_price', 'created_at']
        read_only_fields = ['created_at']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())