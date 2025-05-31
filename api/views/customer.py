from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView
                                     )
from core.serializers import CustomerSerializer
from core.models import Customer
from core.pagination import CustomerPaginator


class CustomerListApiView(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    pagination_class = CustomerPaginator
    

        
class CustomerDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    lookup_url_kwarg = 'pk'
    serializer_class = CustomerSerializer