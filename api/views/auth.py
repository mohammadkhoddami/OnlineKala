from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import User
from core.serializers import SendOtpSerializer, VerifyOtpSerializer
from utils import generate_otp_code, set_value, get_value, delete_value


class SendOtpTokenApi(APIView):
    serializer_class = SendOtpSerializer
    def post(self, request):
        serializer = SendOtpSerializer(data=request.data)
        if serializer.is_valid():
            phone = serializer.validated_data.get('phone', None)
            otp = generate_otp_code()
            set_value(f"otp:{phone}", otp, ttl=3600)
            
            return Response({"message": "OTP SEND", "DEBUG": (otp, phone)}, status=status.HTTP_200_OK)
        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            

class VerifyOtpTokenApi(APIView):
    serializer_class = VerifyOtpSerializer
    def post(self, request):
        phone = request.headers.get("X-PHONE")
        serializer = VerifyOtpSerializer(data=request.data)
        if serializer.is_valid():
            otp = serializer.validated_data.get('otp')
            if not phone or not otp:
                return Response({"error": "phone_number or otp is invalid"})
            
            save_otp = get_value(f"otp:{phone}")
            
            if save_otp != otp:
                return Response({"error": "Otp is Invalid or expired"})
            
            user, created = User.objects.get_or_create(phone_number=phone)
            
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            
            delete_value(f'otp:{phone}')
            
            return Response({
                'access': str(access),
                'refresh': str(refresh),
                'user': str(user.phone_number)
            })