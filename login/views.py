from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode

from .tokens import account_activation_token
from .forms import SignUpForm
from .emails import send_activation_email

def account_activation_sent(request):
    return render(request, 'login/account_activation_sent.html')

def account_activation_invalid(request):
    return render(request, 'login/account_activation_invalid.html')


def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(username=request.POST['username'])
        except User.DoesNotExist:
            user = None

        if user is not None and user.is_active and user.profile.email_confirmed\
          and user.check_password(request.POST['password']):
            auth.login(request, user)
            return redirect('find_post')
        else:
            # Wrong username, wrong password, or account not activated
            # Intended not to show what went wrong for security reasons
            messages.error(request, 'Wrong username password combination.')
            messages.error(request, 'Also please make sure you have activate the account.')

    return render(request, 'login/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


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
    return render(request, 'login/signup.html', {'title': 'Sign Up', 'form': form})


def activate(request, uidb64, token):
    # Try to retrieve uid from the link.
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    # Check whether the token is valid.
    # If so, activate the user's account.
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        auth.login(request, user)
        return redirect('find_post')
    else:
        return render(request, 'account_activation_invalid.html')
