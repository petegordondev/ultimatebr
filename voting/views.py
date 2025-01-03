from django.shortcuts import render, redirect
from .models import Vote, Poll
from .forms import PollForm

def dashboard(request):
    poll = Poll.objects.latest('start_date')  # Example: get the latest poll
    return render(request, 'dashboard/dashboard.html', {'poll': poll})

def vote_panel(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.user = request.user
            vote.save()
            return redirect('vote_history')
    else:
        form = PollForm()
    return render(request, 'voting/vote_panel.html', {'form': form, 'poll': poll})

def vote_history(request):
    votes = Vote.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'voting/vote_history.html', {'votes': votes})