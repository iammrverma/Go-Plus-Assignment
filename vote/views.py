from django.shortcuts import render
from .models import VoteCount

def index(request):
    vote_count = VoteCount.objects.all()
    likes =  vote_count[0].likes
    dislikes =  vote_count[0].dislikes
    data = {
        'likes': likes,
        'dislikes': dislikes
    }
    return render(request, "vote/index.html", data)