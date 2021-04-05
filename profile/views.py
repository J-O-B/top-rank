from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .models import Profile
from django.contrib import messages


@login_required
def profile(request):
    """
    View To Return Homepage
    """
    profile = Profile.objects
    current_user = request.user
    user = current_user.id

    template = "profile/home.html"
    form = UserUpdateForm()
    context = {
        "profile": profile,
        "form": form,
        'on_profile_page': True,
    }

    return render(request, template, context)
