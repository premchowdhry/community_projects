from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

from .tokens import account_activation_token

def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your Community Project Account'
    email_message = render_to_string('login/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token': account_activation_token.make_token(user),
    })
    user.email_user(subject, email_message)

def send_reset_password_email(request, user):
    pass
