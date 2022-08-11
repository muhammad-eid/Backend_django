from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # path('signup_activate/<uidb64>/<token>/', views.signup_activate, name='signup_activate'),
    path('email_verfiy/', views.email_verfiy, name='email_verfiy'),
    # path('dashboard', views.dashboard, name='dashboard')

]