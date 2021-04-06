from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .models import Profile, create_or_update_user_profile
from django.contrib import messages

from datetime import date

today = date.today()


def after_login(request):
    user = request.user
    template = "profile/after-login.html"
    try:
        check = user.profile
    except Exception:
        create_or_update_user_profile(
            sender=user, instance=user, created=today)

    context = {
        "user": user,
    }
    return render(request, template, context)


@login_required
def ProfileView(request):
    """
    A View To Show Basic User Information
    """
    # Try to get the user profile, else create a new instance if none exists

    user = request.user
    profile = get_object_or_404(Profile, user=user)

    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save()
        else:
            pass
    else:
        form = UserUpdateForm(instance=profile)

    template = "profile/profile.html"
    context = {
        "form": form,
        "user": user,
    }

    return render(request, template, context)
