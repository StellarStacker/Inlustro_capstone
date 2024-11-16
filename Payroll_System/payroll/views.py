# payroll/views.py

from django.shortcuts import render, redirect
from joblib.parallel import method

def index(request):
    # This will render the template for the root page (you can customize this)
    return render(request, 'payroll/login.html')

def payslip(request):
    # Render the payslip template
    return render(request, 'payroll/payslip.html')
def dashboard(request):
    return render(request, 'payroll/dashboard.html')

def login(request):
    print("in login")
    if request.method == 'POST':
        # Get username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user (replace with your authentication logic)
        if(username=="admin" and password=="admin"):
            return redirect('dashboard')  # Redirect to the dashboard

