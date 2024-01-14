from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('main/', views.index, name='main'),
    path('allnews/', views.allnews, name='allnews'),
    path('categori/', views.categori, name='categori'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    # dashboard
    path('dashboard', views.dashboard),
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
]