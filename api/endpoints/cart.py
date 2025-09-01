from django.urls import path 
from api.views import (CartApiView, CartDetailApiView,
                       CartItemApiView, CartitemDetailApiView)


app_name = 'cart'


urlpatterns = [
    path('', CartApiView.as_view(), name='cart_list'),
    path('<uuid:pk>/', CartDetailApiView.as_view(), name='cart_detail'),
    path('<uuid:pk>/items/', CartItemApiView.as_view(), name='cart_items'),
    path('<uuid:pk>/items/<uuid:item_pk>/', CartitemDetailApiView.as_view(), name='cart_items_detail')
]



#127.0.0.1:8000/api/v1/cart/<uuid:pk>/items
#127.0.0.1:8000/api/v1/cart/<uuid:pk>/items/<uuid:pk_items>/