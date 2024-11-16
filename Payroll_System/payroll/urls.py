# payroll/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL redirects to 'index' view
    path('login/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
path('dashboard.html', views.dashboard, name='dashboard_html'),

]
