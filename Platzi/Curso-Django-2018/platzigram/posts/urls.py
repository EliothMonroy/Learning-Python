from django.urls import path
from posts import views

urlpatterns = [
    path('', views.list_posts, 'feed'),
    path('new/', views.create_post, 'create_post'),
]
