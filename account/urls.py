from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('login/<str:user_name>/', views.login_user),
     path('profile/', views.profile),
     path('signup/', views.signup),
     path('logout/', views.log_out),
     
]
