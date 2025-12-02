from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend



from core.models import Product
from core.serializers import ProductSerializer
from core.filters import ProductFilterSet


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilterSet
    search_fields = ['title']
    ordering_fields = ['price', 'stash']
    