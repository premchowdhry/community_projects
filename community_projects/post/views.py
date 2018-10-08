from django.shortcuts import render
from .models import Post

def find(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'post/find.html', context)

def create_post(request):
    return render(request, 'post/create.html')

def dashboard(request):
    return render(request, 'post/dashboard.html')

def profile(request):
    return render(request, 'post/profile.html')
