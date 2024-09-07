from django.urls import path
from .views import ProductListView, ProductCreateView, Login, Sign, logout_view, HomeView, ProductDetailView, \
    AddToCartView, CartView, remove_from_cart, PreorderView, paymenthandler, PreOrderListView, home, decrease_quantity, \
    increase_quantity
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/new/', ProductCreateView.as_view(), name='product-create'),
    path('hello', home),
    path('login_view/', Login.as_view(), name='login_view'),
    path('sign/', Sign.as_view(), name='signup'),
    path('logout/user/', logout_view, name='logout_user'),
    path('dashboard/', HomeView.as_view(), name='home'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_to_cart/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/', CartView.as_view(), name='cart'),
    path('cart/increase/<int:pk>/', increase_quantity, name='increase_quantity'),
    path('cart/decrease/<int:pk>/', decrease_quantity, name='decrease_quantity'),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
    path('preorder/', PreorderView.as_view(), name='preorder'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('preorders/', PreOrderListView.as_view(), name='preorder-list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
