from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard/dashboard.html', {'welcome_message': 'Welcome to your Dashboard'})