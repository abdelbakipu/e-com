from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartView, CartItemView

router = DefaultRouter()
router.register('items', CartItemView, basename='cart-item')

urlpatterns = [
    path('', CartView.as_view(), name='cart-detail'),
    path('', include(router.urls)),
]