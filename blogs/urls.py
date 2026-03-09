from django.urls import path
from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blogs_list_view, name='list'),
    path('<int:pk>/', views.blog_detail_view, name='detail'),
]