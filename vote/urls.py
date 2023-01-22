"""
author: Raj Verma
date: 21/01/2023
"""

from django.urls import path
from . import views

urlpatterns = [
    path('vote/like/', views.like, name='like'),
    path('vote/dislike/', views.dislike, name='dislike'),
    path('', views.index, name='index'),
]
