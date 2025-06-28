from rest_framework import serializers
from core.models import Comment, Product
from django.contrib.auth import get_user_model


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'product', 'body', 'status']
        
    def get_author(self, data: Comment):
        if data.author:
            return data.author.last_name
        return None
    
    def create(self, validated_data):
        #Getting pk from ModelViewSet
        request_user = self.context.get('request').user #type: ignore
        product_pk = self.context['product_pk']
        
        if not request_user.is_authenticated:
            raise serializers.ValidationError('You must sign up first')
        
        product = Product.objects.get(pk=product_pk)
        
        return Comment.objects.create(product=product,
                                      author=request_user,
                                      **validated_data)