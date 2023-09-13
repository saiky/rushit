from django.urls import path

from django.shortcuts import render
from accounts import views


urlpatterns = [
	path('', views.IndexView, name="index"),
	path('login', views.LoginView, name="login"),
	path('logout', views.LogoutView, name="logout"),
	path('register', views.RegisterView, name="register"),

]