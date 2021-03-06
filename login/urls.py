from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('account_activation_sent/', views.account_activation_sent, name='account_activation_sent'),
    path('account_activation_invalid/', views.account_activation_invalid, name='account_activation_invalid'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
