from django.shortcuts import render
from .models import Post

def find(request):
    context = {
        'user': request.user,
        'posts': Post.objects.all(),
    }
    return render(request, 'post/find.html', context)

def post(request):
    return render(request, 'post/post.html')

def dashboard(request):
    context = {
        'user': request.user
    }
    return render(request, 'post/dashboard.html')

def profile(request):
    context = {
        'user': request.user
    }
    return render(request, 'post/profile.html')
