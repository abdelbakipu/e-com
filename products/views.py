from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet, generics
from .permissions import IsStaffOrReadOnly
from .models import Category, Product, ProductImage
from .serializers import CategorySerializer, ProductDetailSerializer, ProductListSerializer, ProductImageSerializer
# Create your views here.

class CategoryViewSet(ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    permission_classes = [IsStaffOrReadOnly]    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Product.objects.all()
        return Product.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer
    

class ProductImageCreateListView(generics.ListCreateAPIView):
    serializer_class = ProductImageSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs['product_id'])
    
    def perform_create(self, serializer):
        product = get_object_or_404(Product, pk = self.kwargs['product_id'])
        serializer.save(product=product)