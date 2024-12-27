from django.shortcuts import redirect
from django.conf import settings
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        exempt_paths = [
            reverse('account_login'),  # Allauth login
            reverse('account_signup'),  # Allauth signup
            reverse('account_reset_password'),  # Allauth password reset
            reverse('account_reset_password_done'),  # Allauth password reset done
            reverse('account_logout'),  # Allauth logout
            reverse('admin:index'),  # Admin panel
        ]

        if not request.user.is_authenticated and request.path not in exempt_paths:
            return redirect(settings.LOGIN_URL)

        return self.get_response(request)