from django.contrib import admin
from .models import Subject, VotingItem, Poll

admin.site.register(Subject)
admin.site.register(VotingItem)
admin.site.register(Poll)
