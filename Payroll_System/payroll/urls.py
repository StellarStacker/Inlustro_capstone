# payroll/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),  # Root URL redirects to 'index' view
    path('payslip/', views.payslip, name='payslip'),
]
