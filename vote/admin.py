from django.contrib import admin

# Register your models here.
from .models import VoteCount

admin.site.register(VoteCount)