from django.shortcuts import render
from .models import VoteCount

vote_count = VoteCount.objects.all()

def index(request):
    data = {
        'likes': vote_count[0].likes,
        'dislikes': vote_count[0].dislikes
    }
    return render(request, "vote/index.html", data)