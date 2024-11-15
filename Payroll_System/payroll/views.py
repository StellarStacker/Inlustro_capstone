# payroll/views.py

from django.shortcuts import render

def index(request):
    # This will render the template for the root page (you can customize this)
    return render(request, 'login.html')

def payslip(request):
    # Render the payslip template
    return render(request, 'payslip.html')
