from django.utils.text import slugify
from rest_framework import serializers
from core.models import Product



class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'title', 'slug', 'categoory', 'price', 'body', 'stash', 'active')
        read_only_fields = ('slug', )
        
    
    def create(self, validated_data):
        product = Product(**validated_data)
        product.slug = slugify(validated_data.get('title'))
        product.save()
        return product