from django.db import models

# Create your models here.
class VoteCount(models.Model):
    likes = models.IntegerField()
    dislikes = models.IntegerField()