from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Order, OrderItem, Customer, Product, Cart, CartItem
from core.services import create_order_from_cart


class CustomerOrderSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(source='user.phone_number')
    class Meta:
        model = Customer
        fields = ['phone_number', 'age']

class OrderItemProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'active']

class OrderItemSerializer(serializers.ModelSerializer):
    product = OrderItemProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerOrderSerializer()
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'items']
        

class OrderCreateSerializer(serializers.Serializer):
    cart_id = serializers.UUIDField()
    
    def validate_cart_id(self, cart_id):
        
        if not Cart.objects.filter(pk=cart_id).exists():
            raise serializers.ValidationError("there is no cart")
        
        if CartItem.objects.filter(cart_id=cart_id).count() == 0:
            raise serializers.ValidationError("Empty")
        
        return cart_id
        
    def save(self, **kwargs):
        cart_id = self.validated_data['cart_id']
        user = self.context['user']
        return create_order_from_cart(cart_id=cart_id, user=user)