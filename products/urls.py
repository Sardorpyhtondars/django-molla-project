from django.urls import path
from products.views import product_list_view, product_detail_view, cart_view, checkout_view, wishlist_view

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('wishlist/', wishlist_view, name='wishlist'),
]