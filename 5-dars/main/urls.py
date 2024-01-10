from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('index.html', index),
    path('about.html', about),
    path('services.html', services),
    path('pricing.html', pricing),
    path('car.html', car),
    path('blog.html', blog),
    path('contact.html', contact),
    path('blog-single.html', blog_single),
]