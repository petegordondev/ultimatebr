from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Poll(models.Model):  # Renamed from VotingPanel
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title


class VotingItem(models.Model):
    panel = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='items', default=1)  # Updated reference
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.subject.name} in {self.panel.title}"
    
class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voting_item = models.ForeignKey(VotingItem, on_delete=models.CASCADE, related_name='votes', default=1)
    vote = models.BooleanField()  # True for yes, False for no
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'voting_item')  # Prevents duplicate votes by the same user on the same item

    def __str__(self):
        return f"{self.user} voted {self.vote} on {self.voting_item}"
