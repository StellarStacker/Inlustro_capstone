
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Hardcoded credentials
USERNAME = 'admin'
PASSWORD = 'admin123'

# Index view (Login page)
def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the credentials match
        if username == USERNAME and password == PASSWORD:
            # Manually log the user in by setting session data
            request.session['user_logged_in'] = True
            return redirect('admin_dashboard')  # Redirect to dashboard on successful login

        else:
            return HttpResponse('Invalid credentials', status=401)  # Invalid credentials

    return render(request, 'payroll/login.html')  # Render login page

# Dashboard view (accessible after successful login)
def admin_dashboard(request):
    return render(request, 'payroll/admin_dashboard.html')
def dashboard(request):
    if not request.session.get('user_logged_in', False):
        return redirect('index')  # Redirect to login if not authenticated

    # Sample employees data (could be replaced with database data)
    employees = [
        {'name': "John Doe", 'role': "Manager", 'hourly_rate': 50, 'hours_worked': 40},
        {'name': "Jane Smith", 'role': "Manager", 'hourly_rate': 55, 'hours_worked': 45},
        {'name': "Mike Johnson", 'role': "Staff", 'hourly_rate': 30, 'hours_worked': 38},
        {'name': "Emily Davis", 'role': "Staff", 'hourly_rate': 28, 'hours_worked': 42},
    ]

    # Render the dashboard template with employee data
    return render(request, 'dashboard.html', {'employees': employees})

# Logout view
def logout_view(request):
    # Clear session data to log the user out
    request.session.flush()
    return redirect('index')  # Redirect to login page after logout
