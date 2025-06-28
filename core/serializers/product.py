from decimal import Decimal
from django.utils.text import slugify
from rest_framework import serializers
from core.models import Product



class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'categoory', 'price', 'body', 'stash', 'active', 'final_price')
        read_only_fields = ('slug', )
        
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.slug = slugify(validated_data.get('title'))
        product.save()
        return product
    
    def get_final_price(self, product: Product):
        return round(Decimal(product.price) * Decimal(1.09), 2)
    
    def validate(self, attrs):
        if len(attrs['title']) < 3:
            raise serializers.ValidationError('title at least must be 4')
        return attrs
    
    def validate_title(self, data: str):
        if data.isnumeric():
            raise serializers.ValidationError('Must contains alpha')
        return data