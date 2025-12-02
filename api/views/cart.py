from django.utils.functional import cached_property
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny

from core.models import Cart, CartItem
from core.serializers import (CartSerializer, CartItemSerializer,
                              AddCartItemSerializer, UpdateCartItemSerializer)


#CRUD --> Craete , List
class CartApiView(APIView):
    serializer_class = CartSerializer
    # permission_classes = [IsAdminUser]
    
    def get_permissions(self):
        
        if self.request.method == "POST":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
            
        return [permission() for permission in permission_classes]
    
    
    def get(self, request):
        cart = Cart.objects.all()
        serializer = self.serializer_class(cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#CRUD --> Retrieve, Update, delete
class CartDetailApiView(APIView):
    serializer_class = CartSerializer
    
    @cached_property
    def cart(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'])
    
    
    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        self.cart.delete()
        return Response({'detail': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    
    
class CartItemApiView(APIView):
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        return CartItemSerializer
    
    @cached_property
    def cart(self):
        return get_object_or_404(Cart, pk=self.kwargs['pk'])
    
    def get(self, request, *args, **kwargs):
        item = self.cart.items.select_related('product') #type: ignore
        serializer = self.get_serializer_class()(item, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    def post(self, request, *args, **kwargs):
        serialzier = self.get_serializer_class()(data=request.data, context={'cart':self.cart})
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CartitemDetailApiView(APIView):
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    @cached_property
    def cart_item(self):
        return get_object_or_404(
            CartItem,
            cart__pk=self.kwargs['pk'],
            pk=self.kwargs['item_pk']
        )
        
    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(self.cart_item)
        print(self.cart_item)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(self.cart_item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, *args, **kwargs):
        self.cart_item.delete()
        return Response({'message': 'deleted'}, status=status.HTTP_204_NO_CONTENT)
    
    