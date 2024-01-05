from django.urls import path

from email_verification.views import check_email, email_delete, home, show_results

urlpatterns = [
    path("", home, name="home"),
    path("check/", check_email, name="email-check"),
    path("results/", show_results, name="email-results"),
    path("delete/", email_delete, name="email-delete"),
]
