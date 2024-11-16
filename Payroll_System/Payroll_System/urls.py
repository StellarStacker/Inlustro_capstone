from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('payroll.urls')),
    path('login/', include('payroll.urls')),
    # Ensure 'your_app_name' is correct
    path('payslip/', include('payroll.urls')),
    path('index/dashboard/', include('payroll.urls')),
     # This line maps the root path to your app
]
