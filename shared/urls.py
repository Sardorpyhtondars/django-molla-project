from django.urls import path
from shared.views import home_page_view, about_us_view, contact_view, page_404_view

app_name = 'shared'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about/', about_us_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('404/', page_404_view)
]