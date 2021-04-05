from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    """
    View To Return Homepage
    """
    name = User
    template = "profile/home.html"
    context = {
        "name": name,
        'on_profile_page': True,
    }

    return render(request, template, context)
