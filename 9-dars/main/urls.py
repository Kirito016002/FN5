from django.urls import path
from . import views

urlpatterns = [
    #dashboard
    path('', views.dashboard, name='dashboard'),
    # About me
    path('about_me_list', views.about_me_list, name='about_me_list'),    
    path('about_me_deteil/<int:id>/', views.about_me_deteil, name='about_me_deteil'),    
    path('about_me_delete/<int:id>/', views.about_me_delete, name='about_me_delete'),    
    path('about_me_create', views.about_me_create, name='about_me_create'),   
    # Equpments
    path('equpment', views.equpment_list, name='equpment'),    
    path('equpment_deteil/<int:id>/', views.equpment_deteil, name='equpment_deteil'),    
    path('equpment_delete/<int:id>/', views.equpment_delete, name='equpment_delete'),    
    path('equpment_create', views.equpment_create, name='equpment_create'),    
]