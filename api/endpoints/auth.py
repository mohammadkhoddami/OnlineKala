from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from api.views import SendOtpTokenApi, VerifyOtpTokenApi

app_name = 'auth'

urlpatterns = [
    path('send-otp/', SendOtpTokenApi.as_view(), name='send_otp'),
    path('verify-otp/', VerifyOtpTokenApi.as_view(), name='verify_otp'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('logout/', TokenBlacklistView.as_view(), name='logout'),
] 