from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Dashboard
from .forms import DashboardForm


def dashboard(request):
    if request.method == 'POST':
        form = DashboardForm(request.POST)
        if form.is_valid():
            save_post(request.user, form)
            return redirect('dashboard')
    else:
        form = DashboardForm()
    return render(request, 'post/dashboard.html', {'form': form, 'dashboards': shown_dashboards()})


def shown_dashboards():
    dashboards = Dashboard.objects.all().order_by('-date_posted')
    for dashboard in dashboards:
        dashboard.elapsed_time = elapsed_time(dashboard.date_posted)
    return dashboards


def elapsed_time(date_posted):
    return str(int((timezone.now() - date_posted).total_seconds())) + ' seconds ago'


def save_post(author, form):
    new_post = form.save(commit=False)
    new_post.author = author
    new_post.date_posted = timezone.now()
    new_post.title = form.cleaned_data['title']
    new_post.content = form.cleaned_data['content']
    new_post.save()
