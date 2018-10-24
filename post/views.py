from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Post
from .forms import PostForm

def find(request):
    context = {
        'user': request.user,
        'posts': Post.objects.all()[:6],
    }
    return render(request, 'post/find.html', context)

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            save_post(request.user, form)
            return redirect('find_post')
    else:
        form = PostForm()
    return render(request, 'post/post.html', {'form': form})

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

def save_post(author, form):
    new_post = form.save(commit=False)
    new_post.author = author
    new_post.date_posted = timezone.now()
    new_post.save()
