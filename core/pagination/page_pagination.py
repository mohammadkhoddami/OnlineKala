from rest_framework.pagination import PageNumberPagination



class CustomerPaginator(PageNumberPagination):
    page_size = 3