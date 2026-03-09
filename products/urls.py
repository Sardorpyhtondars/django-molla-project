from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.product_list_view, name='list'),
    path('<int:pk>/', views.product_detail_view, name='detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('wishlist/', views.wishlist_view, name='wishlist'),
]