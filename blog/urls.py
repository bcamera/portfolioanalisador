from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list,name = 'post_list'),
    path('sobre/', views.about, name = 'about'),                                                                                  
    path('contato/', views.contact, name = 'contact'),
] 
