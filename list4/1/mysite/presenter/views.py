from django.shortcuts import render, redirect
from functions import get_posts, get_friends

posts_token = None
friends_token = None

def index(request):
    return redirect('posts')

def posts(request):
    context = {}
    if posts_token:
        context['posts'] = get_posts(posts_token)
    return render(request, 'presenter/posts.html', context)

def friends(request):
    context = {}
    if friends_token:
        context['friends'] = get_friends(friends_token)
    return render(request, 'presenter/friends.html', context)