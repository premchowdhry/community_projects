from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from .forms import SignUpForm
from .tokens import account_activation_token

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
            current_site = get_current_site(request)
            subject = 'Activate Your Community Project Account'
            email_message = render_to_string('login/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, email_message)
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
        return redirect('login')
    else:
        return render(request, 'account_activation_invalid.html')
