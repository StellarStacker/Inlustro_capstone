# Payroll_System/urls.py

from django.contrib import admin
from django.urls import path, include  # include is necessary to include app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('django.contrib.auth.urls')),  # Default login URL
    path('payslip/', include('payroll.urls')),  # Include the 'payroll' app URLs
]
