from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.find, name='find_post'),
    path('create/', views.create_post, name='create_post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
]
