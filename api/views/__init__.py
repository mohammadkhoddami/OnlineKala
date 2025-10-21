from .category import CategoryListApiView, CategoryDetailApiView
from .customer import CustomerListApiView, CustomerDetailApiView
from .product import ProductViewSet
from .comments import CommentViewSet
from .cart import CartApiView, CartDetailApiView, CartItemApiView, CartitemDetailApiView
from .order import OrderViewSet
from .auth import SendOtpTokenApi, VerifyOtpTokenApi