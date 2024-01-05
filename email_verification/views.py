"""Module for handling views in the email verification application."""


import os
from http import HTTPStatus

import requests
from django.contrib import messages
from django.shortcuts import redirect, render, reverse
from dotenv import load_dotenv

from email_verification.forms import EmailCheckForm, EmailDeleteForm
from email_verification.models import Email

# Create your views here.
load_dotenv()

API_KEY = os.getenv("API_KEY")
TIMEOUT = 5  # seconds
FORM_KEY = "form"


def home(request):
    """
    Render and returns the home page.

    This view function renders the home page of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page as an HTTP response.
    """
    return render(request, "home.html")


def verify_email_via_api(email: str):
    """
    Verify an email address using an external API.

    This function sends a GET request to an email verification service and
    retrieves the verification results in JSON format.

    Args:
        email (str): The email address that needs to be verified.

    Returns:
        dict or None: A dictionary containing the verification results if the
        request is successful; otherwise, None.
    """
    response = requests.get(
        "https://api.hunter.io/v2/email-verifier?email={0}&api_key={1}".format(
            email,
            API_KEY,
        ),
        timeout=TIMEOUT,
    )
    if response.status_code == HTTPStatus.OK:
        return response.json().get("data", {})
    return None


def save_email(email_data: dict):
    """
    Save email information to the database.

    This function takes a dictionary containing email details and creates
    a new Email record in the database using this information.

    Args:
        email_data (dict): A dictionary with keys 'email', 'score', and 'status'.
    """
    email_record = Email(
        email=email_data.get("email"),
        score=email_data.get("score"),
        status=email_data.get("status"),
    )
    email_record.save()


def check_email(request):
    """
    Process an email check request and update the database accordingly.

    This view function handles POST requests with email data, verifies if the email
    already exists in the database, and if not, verifies it using an external API.
    Based on the results, it updates the database and informs the user.

    Args:
        request (HttpRequest): The HTTP request object from Django.

    Returns:
        HttpResponse: The rendered email check page with form and possible messages.
    """
    form = EmailCheckForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        email = form.cleaned_data.get("email")
        if Email.objects.filter(email=email).exists():
            messages.error(request, "This email is already in the database.")
        else:
            email_data = verify_email_via_api(email)
            if email_data:
                save_email(email_data)
                messages.success(request, "Email was checked successfully!")
            else:
                messages.error(request, "Failed to verify the email.")

    return render(request, "email/check.html", {FORM_KEY: form})


def show_results(request):
    """Display all the email records from the database.

    This view retrieves all email records from the database and displays them.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered page showing all email records.
    """
    emails = Email.objects.all()
    return render(request, "email/show_all.html", {"emails": emails})


def email_delete(request):
    """Handle the deletion of an email record.

    This view allows users to delete an email record from the database. It uses a form
    to get the email to be deleted and then removes it from the database if it exists.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered page for email deletion with form and possible messages.
    """
    form = EmailDeleteForm(request.POST)
    if form.is_valid():
        email_to_delete = form.cleaned_data.get("email")
        try:
            email_obj = Email.objects.get(email=email_to_delete)
        except Email.DoesNotExist:
            messages.error(request, "This email doesn't exist in the database.")
            return render(request, "email/delete_record.html", {FORM_KEY: form})

        email_obj.delete()
        messages.success(request, "Email has been successfully deleted.")
        return redirect(reverse("email-results"))
    else:
        form = EmailDeleteForm()

    return render(request, "email/delete_record.html", {FORM_KEY: form})
