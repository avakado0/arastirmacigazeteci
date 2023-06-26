from django.shortcuts import render
from .models import Topic
from django.db import models

def community_home(request):
    # Add your home view logic here
    return render(request, 'community/community_home.html')

def topic_list(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'community/topic_list.html', context)

def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    context = {'topic': topic}
    return render(request, 'community/topic_detail.html', context)
