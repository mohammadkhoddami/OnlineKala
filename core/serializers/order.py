from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Order, OrderItem, Customer, Product


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
        fields = ['order', 'product', 'quantity', 'unit_price']

class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerOrderSerializer()
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'customer', 'status', 'items']
        
