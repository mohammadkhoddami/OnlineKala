from django_filters.rest_framework import FilterSet


from core.models import Product


class ProductFilterSet(FilterSet):
    class Meta:
        model = Product
        fields = {
            'stash': ['lt', 'gt', 'exact'] # stash > 10  stash < 10 stash == 10
         }