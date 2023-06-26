from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community_home, name='community_home'),
    path('topics/', views.topic_list, name='topic_list'),
    path('topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
]
