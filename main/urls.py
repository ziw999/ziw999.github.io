from django.urls import path
from django.views.decorators.cache import cache_page
from . import views

app_name='main'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about', cache_page(60)(views.AboutView.as_view()), name='about'),
    path('contacts', cache_page(60)(views.ContactView.as_view()), name='contacts'),
    path('delivery', cache_page(60)(views.DeliveryView.as_view()), name='delivery'),
]