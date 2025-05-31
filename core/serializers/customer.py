from rest_framework import serializers
from core.models import Customer
from django.contrib.auth import get_user_model


class UserCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'phone_number', 'first_name', 'last_name', 'is_staff']


class CustomerSerializer(serializers.ModelSerializer):
    user = UserCustomerSerializer(read_only=True)
    
    class Meta:
        model = Customer
        fields = ['id', 'user', 'age']