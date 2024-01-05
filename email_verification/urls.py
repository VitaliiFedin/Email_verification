from django.urls import path

from email_verification.views import check_email, home

urlpatterns = [
    path("", home, name="home"),
    path("check/", check_email, name="email-check"),
]
