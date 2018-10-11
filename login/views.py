from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from .tokens import account_activation_token
from .forms import SignUpForm
from .emails import send_activation_email


def login(request):
    return render(request, 'login/login.html')

def account_activation_sent(request):
    return render(request, 'login/account_activation_sent.html')

def account_activation_invalid(request):
    return render(request, 'login/account_activation_invalid.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            send_activation_email(request, user)
            return redirect('account_activation_sent')
        else:
            messages.error(request, f'Error')
    else:
        form = SignUpForm()

    context = {
        'title': 'Sign Up',
        'form': form,
    }
    return render(request, 'login/signup.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        auth.login(request, user)
        return redirect('find_post')
    else:
        return render(request, 'account_activation_invalid.html')
