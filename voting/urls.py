from django.urls import path
from .views import vote, vote_history

urlpatterns = [
    path('vote/', vote, name='vote'),
    path('history/', vote_history, name='vote_history'),
]