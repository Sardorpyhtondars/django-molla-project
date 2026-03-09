from django.urls import path
from shared import views

app_name = 'shared'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('about/', views.about_us_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]