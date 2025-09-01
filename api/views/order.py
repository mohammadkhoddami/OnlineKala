from django.db.models import Prefetch
from rest_framework.viewsets import ModelViewSet
from core.models import Order, OrderItem
from core.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):    
    def get_serializer_class(self):
        if self.request.method == "POST":
            pass
        return OrderSerializer
    
    def get_queryset(self):
        queryset = Order.objects \
            .select_related('customer__user') \
            .prefetch_related(
                Prefetch(
                    'items', 
                    queryset=OrderItem.objects.select_related('product')
                )
            ).all()
        
        if self.request.user.is_staff:
            return queryset
        
        return queryset.filter(customer__user=self.request.user)
            
