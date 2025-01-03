from django.shortcuts import render, redirect
from .models import Vote
from .forms import VoteForm

def vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('vote_history')
    else:
        form = VoteForm()
    return render(request, 'voting/vote.html', {'form': form})

def vote_history(request):
    votes = Vote.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'voting/vote_history.html', {'votes': votes})