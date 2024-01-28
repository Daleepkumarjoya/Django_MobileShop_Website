from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.HomePage, name="Home"),
    path('ViewPage/<int:id>', views.ViewPage, name="View"),
    path('checkout/<int:id>', views.checkout, name="checkout"),
    path('aboutPage/', views.aboutPage, name="About"),
    path('contactUsPage/', views.contactUsPage, name="contact"),
    path('registerPage/', views.registerPage, name="register"),
    path('logInPage/', views.logInPage, name="LogIn"),
    path('logOutPage/', views.logOutPage, name="LogOut"),
]
