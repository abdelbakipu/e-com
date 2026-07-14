from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .serializers import CartItemSerializer, CartSerializer
from .models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user = self.request.user)
        return cart

class CartItemView(ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user = self.request.user)
    
    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user = self.request.user)
        serializer.save(cart = cart)