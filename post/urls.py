from django.urls import path
from . import views

urlpatterns = [
    path('find/', views.find, name='find_post'),
    path('post/', views.post, name='post'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('signed_up_post/', views.signed_up_post, name='signed_up_post'),
]
