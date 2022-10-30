from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('rest/', views.restdata_show, name = 'rest'),
    path('login_page/', views.login_page, name = 'login_page'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path("register/", views.register_request, name="register"),
    path("menu/", views.search, name="menu"),
    path('detail/<int:pk>/',views.detail, name = 'details'),

    

    
    
]