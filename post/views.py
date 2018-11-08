from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Post
from .forms import PostForm


def find(request):
    return render(request, 'post/find.html', {'posts': shown_posts(request)})


def dashboard(request):
    return render(request, 'post/dashboard.html')


def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            save_post(request.user, form)
            return redirect('find_post')
    else:
        form = PostForm()
    return render(request, 'post/post.html', {'form': form})


def profile(request):
    return render(request, 'post/profile.html')


def save_post(author, form):
    new_post = form.save(commit=False)
    new_post.author = author
    new_post.date_posted = timezone.now()
    new_post.save()


def shown_posts(request):
    posts = Post.objects.all().order_by('-date_posted')
    if 'type' in request.GET:
        if request.GET['type'] != 'any':
            posts = posts.filter(type=request.GET['type'])
    if 'estimate_hours' in request.GET:
        h = request.GET['estimate_hours']
        if h == '<1_hour':
            posts = posts.filter(estimate_hours__range=(0, 1))
        elif h == '<3_hours':
            posts = posts.filter(estimate_hours__range=(2, 3))
        elif h == '<5_hours':
            posts = posts.filter(estimate_hours__range=(4, 5))
        elif h == '>5_hours':
            posts = posts.filter(estimate_hours__gte=6)
    if 'work_date' in request.GET:
        d = request.GET['work_date']
        if d == 'this_week':
            posts = posts.filter(
                work_date__lte=timezone.now() + timezone.timedelta(days=7))
        elif d == 'this_month':
            posts = posts.filter(
                work_date__lte=timezone.now() + timezone.timedelta(days=30))
        elif d == 'within_3_months':
            posts = posts.filter(
                work_date__lte=timezone.now() + timezone.timedelta(days=90))
        elif d == 'within_6_months':
            posts = posts.filter(
                work_date__lte=timezone.now() + timezone.timedelta(days=180))
    return posts[:]


def signed_up_post(request):
    return render(request, 'post/signed_up_post.html')
