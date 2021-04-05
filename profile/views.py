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
    try:
        profile = user.profile
    except Exception:
        profile = False
    # See if a user profile exists, if not create one for that user
    if profile:
        profile = user.profile
        message = "To Edit Your Profile, Fill Out The Form Below"
    else:
        create_or_update_user_profile(
            sender=user, instance=user, created=today)
        profile = user.profile
        message = "It seems like you didn't have a profile on record, \
            please update your information below:"

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
        else:
            pass
    else:
        form = UserUpdateForm(instance=profile)

    template = "profile/home.html"
    form = UserUpdateForm()
    context = {
        'message': message,
        "profile": profile,
        "form": form,
        'on_profile_page': True,
    }

    return render(request, template, context)
