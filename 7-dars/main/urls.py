from django.urls import path
from . import views

urlpatterns = [
    # front
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('news', views.news, name='news'),
    # dashboard
    path('dashboard', views.dashboard),
    path('dashboard/region/create', views.create_region, name='create_region'),
    path('dashboard/region/list', views.regions, name='regions'),
    path('dashboard/region/update/<int:id>/', views.region_update, name='region_update'),
    path('dashboard/region/delete/<int:id>/', views.region_delete, name='region_delete'),
    # dashboard category CRUD
    path('dashboard/category/list', views.category_list, name='list'),
    path('dashboard/category/create', views.category_create, name='create'),
    path('dashboard/category/update/<int:id>/', views.category_update, name='update'),
    path('dashboard/category/delete/<int:id>/', views.category_delete, name='delete'),
]