from django.shortcuts import render

from .forms import EmailCheckForm123

# Create your views here.


def home(request):
    """Renders and returns the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page as an HTTP response.
    """
    return render(request, "_base.html")


def check_email(request):
    """_summary_

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == "POST":
        form = EmailCheckForm123(request.POST)
        if form.is_valid():
            print("good")
    else:
        form = EmailCheckForm123()
    return render(request, "email/check.html", {"form": form})
