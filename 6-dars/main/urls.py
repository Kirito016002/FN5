from django.urls import path
from .views import (index, allnews, categori, contact)

urlpatterns = [
    path('', index),
    path('main/', index, name='main'),
    path('allnews/', allnews, name='allnews'),
    path('categori/', categori, name='categori'),
    path('contact/', contact, name='contact'),
]