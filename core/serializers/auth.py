import re
from rest_framework import serializers

class SendOtpSerializer(serializers.Serializer):
    phone = serializers.CharField()
    
    def validate_phone(self, value):
        if not re.match(r'^09\d{9}$', value):
            serializers.ValidationError("Phone Number Is Not Correct")
        return value
    

class VerifyOtpSerializer(serializers.Serializer):
    otp = serializers.CharField()