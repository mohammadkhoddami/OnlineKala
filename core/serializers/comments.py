from rest_framework import serializers
from core.models import Comment, Product


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'author', 'body', 'status']
        extra_kwargs = {'status': {'read_only': True}}
        
    def get_author(self, data: Comment):
        if data.author:
            return data.author.last_name
        return None
    
    def create(self, validated_data):
        #Getting pk from ModelViewSet
        request_user = self.context.get('request').user #type: ignore
        product_pk = self.context['product_pk']
        print(product_pk, request_user)
        
        
        if not request_user.is_authenticated:
            raise serializers.ValidationError('You must sign up first')
        
        product_instance = Product.objects.get(pk=product_pk)
        
        return Comment.objects.create(product=product_instance,
                                      author=request_user,
                                      **validated_data)