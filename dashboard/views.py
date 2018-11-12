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
    time = int((timezone.now() - date_posted).total_seconds())
    if time >= 86400:
        time //= 86400
        return str(time) + (' day ago' if (time == 1) else ' days ago')
    if time >= 3600:
        time //= 3600
        return str(time) + (' hour ago' if (time == 1) else ' hours ago')
    if time >= 60:
        time //= 60
        return str(time) + (' minute ago' if (time == 1) else ' minutes ago')
    return str(time) + ' seconds ago'



def save_post(author, form):
    new_post = form.save(commit=False)
    new_post.author = author
    new_post.date_posted = timezone.now()
    new_post.content = form.cleaned_data['content']
    new_post.save()
