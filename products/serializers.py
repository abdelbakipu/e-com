from rest_framework import serializers
from .models import Category, Product, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['id']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'is_primary']
        read_only_fields = ['id','product']

class ProductListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field = 'name',
        queryset = Category.objects.all()
    )
    primary_image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'price', 'category', 'primary_image', 'is_active']
        read_only_fields = ['id']

    def get_primary_image(self, obj):
        image = obj.images.filter(is_primary=True).first()
        if image:
            return ProductImageSerializer(image, context=self.context).data
        return None
    
class ProductDetailSerializer(ProductListSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta(ProductListSerializer.Meta):
        fields = ProductListSerializer.Meta.fields + ['description', 'images', 'stock', 'created_at']