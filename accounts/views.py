from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


def dashboard(request):
    """
    View to return the user dashboard
    """
    return render(request, 'accounts/dashboard.html')


def edit(request):
    """
    View to return the user dashboard
    pass in the id of the user, then we can connect class in
    models to update profile.
    """
    return render(request, 'accounts/edit.html')


def register(request):
    """
    View to return the user dashboard
    pass in the id of the user, then we can connect class in
    models to update profile.
    """

    form = UserProfileForm()

    template = 'accounts/register.html'
    context = {
        'form': form,
        'on_profile_page': True,
    }

    return render(request, template, context)
