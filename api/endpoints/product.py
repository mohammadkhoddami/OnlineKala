from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet

app_name = 'product'

router = DefaultRouter()

router.register('', ProductViewSet, basename='product')

urlpatterns = router.urls