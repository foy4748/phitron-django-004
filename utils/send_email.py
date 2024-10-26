# Email Related
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


def success_email(
    request,
    subject,
    message,
    success_url="/",
    domain="https://phitron-django-004.onrender.com",
):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    context = {
        "username": request.user.username,
        "message": message,
        "success_url": success_url,
        "domain": domain,
    }
    html_message = render_to_string("email_template.html", context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, sender, recipient_list)
    email.attach_alternative(html_message, "text/html")
    email.send()


def failure_email(
    request,
    subject,
    message,
    success_url="/",
    domain="https://phitron-django-004.onrender.com",
):
    sender = settings.EMAIL_HOST_USER
    recipient_list = [request.user.email]
    context = {
        "username": request.user.username,
        "message": message,
        "success_url": success_url,
        "domain": domain,
    }
    html_message = render_to_string("email_template.html", context)
    plain_message = strip_tags(html_message)
    email = EmailMultiAlternatives(subject, plain_message, sender, recipient_list)
    email.attach_alternative(html_message, "text/html")
    email.send()
