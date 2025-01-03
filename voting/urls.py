from django.urls import path
from .views import vote_panel, vote_history, dashboard

urlpatterns = [
    path('', dashboard, name='dashboard'),  # Added dashboard view
    path('vote/<int:poll_id>/', vote_panel, name='vote_panel'),
    path('history/', vote_history, name='vote_history'),
]