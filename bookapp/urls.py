from django.contrib import admin
from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.Signup, name='signup'),
    path('signup', views.Signup, name='signup'),
    path('userlogin', views.Login, name='userlogin'),
    path('home', views.Home, name='home'),
    path('register', views.UserRegister.as_view(), name='regsiter'),
    path('addbook', views.AddBook.as_view(), name='addbook'),
    path('removebook', views.RemoveBook.as_view(), name='removebook'),
    path('logout', views.Logout, name='logout'),
]
