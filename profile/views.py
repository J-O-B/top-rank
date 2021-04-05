from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .models import Profile, create_or_update_user_profile
from django.contrib import messages

from datetime import date

today = date.today()


@login_required
def profile(request):
    """
    View To Return Homepage
    """
    user = request.user
    if user:
        profile = "found"
        create_or_update_user_profile(
            sender=user, instance=user, created=today)
    else:
        profile = "not found"

    template = "profile/home.html"
    form = UserUpdateForm()
    context = {
        "profile": profile,
        "form": form,
        'on_profile_page': True,
    }

    return render(request, template, context)
