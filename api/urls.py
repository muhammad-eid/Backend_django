from django.contrib import admin
from django.urls import path
from . import views

from project import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.connect, name='connect'),
    # path('login/', views.login, name='login'),
    path('activate/', views.activate, name='activate'),
    path('check/', views.check, name='check'),
]