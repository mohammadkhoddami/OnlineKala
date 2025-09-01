from django.urls import path, include
from rest_framework_nested import routers
from api.views import ProductViewSet, CommentViewSet

app_name = 'product'

router = routers.DefaultRouter() #type: ignore

router.register('',
                ProductViewSet,
                basename='product')


product_router = routers.NestedDefaultRouter(router,
                                             '',
                                             lookup='product') #type: ignore


product_router.register('comments', CommentViewSet, basename='product_comment')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(product_router.urls))
]

# 127.0.0.1:8000/api/v1/product/1/comment