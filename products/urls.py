from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ProductImageCreateListView

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='category')
router.register('products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('products/<int:product_id>/images/', ProductImageCreateListView.as_view(), name='product-images'),
]