from django.shortcuts import render, HttpResponse
from .models import VoteCount
import json

def like(request):
    vote_count = VoteCount.objects.all()[0]
    vote_count.likes += 1
    vote_count.save()
    data = {
        'likes': vote_count.likes,
        'dislikes': vote_count.dislikes
    }
    return HttpResponse(json.dumps(data))

def dislike(request):
    vote_count = VoteCount.objects.all()[0]
    vote_count.dislikes += 1
    vote_count.save()
    data = {
        'likes': vote_count.likes,
        'dislikes': vote_count.dislikes
    }
    return HttpResponse(json.dumps(data))

def index(request):
    vote_count = VoteCount.objects.all()[0]
    data = {
        'likes': vote_count.likes,
        'dislikes': vote_count.dislikes
    }
    return render(request, "vote/index.html", data)
