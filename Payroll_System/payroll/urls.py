from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Login page
    path('index/dashboard/', views.admin_dashboard, name='dashboard'),  # Dashboard page after login
    path('logout/', views.logout_view, name='logout'),  # Logout page
]
