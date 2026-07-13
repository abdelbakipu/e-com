from rest_framework import serializers
from accounts.serializer import UserProfileSerializer
from products.serializers import ProductListSerializer
from .models import Cart, CartItem


class CartItemSerializer(serializers.ModelSerializer):
    product_detail = ProductListSerializer(source = 'product', read_only = True)

    class Meta:
        model = CartItem
        fields = ['product','product_detail', 'quantity']

class CartSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer()
    items = CartItemSerializer(many = True, read_only = True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['user', 'items', 'total_price', 'created_at']
        read_only_fields = ['user', 'created_at']

    def get_total_price(self, obj):
        return sum(item.product.price * item.quantity for item in obj.items.all())