from django.urls import path

from . import views
urlpatterns = [
    path('', views.mod_dashboard_overview, name='mod_dashboard_overview'),
    path('control/', views.mod_dashboard_control, name='mod_dashboard_control'),
    path('settings', views.mod_dashboard_settings, name='mod_dashboard_settings'),
]