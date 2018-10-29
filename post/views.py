from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Post
from .forms import PostForm


def find(request):
    return render(request, 'post/find.html', {'posts': shown_posts()})


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
    return render(request, 'post/dashboard.html')


def profile(request):
    return render(request, 'post/profile.html')


def save_post(author, form):
    new_post = form.save(commit=False)
    new_post.author = author
    new_post.date_posted = timezone.now()
    new_post.save()


def shown_posts():
    return Post.objects.all().order_by('-date_posted')[:6]
