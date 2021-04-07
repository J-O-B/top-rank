from django.shortcuts import (render, get_object_or_404,
                              redirect, reverse)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from .models import Profile, create_or_update_user_profile
from django.contrib import messages
from messenger.models import CustomMessage
from messenger.forms import DirectMessage

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
    messages = CustomMessage.objects.all()
    try:
        inbox = CustomMessage.objects.filter(reciever=user)
        outbox = CustomMessage.objects.filter(sender=user)
        inboxcount = CustomMessage.objects.filter(reciever=user).count()
        outboxcount = CustomMessage.objects.filter(sender=user).count()
    except Exception:
        inbox = None
        outbox = None

    if request.method == "POST":
        form1 = UserUpdateForm(request.POST, request.FILES, instance=profile)
        if form1.is_valid():
            profile = form1.save()

        form2 = DirectMessage(request.POST, instance=user)
        if form2.is_valid():
            messages = form2.save()
        
    else:
        form1 = UserUpdateForm(instance=profile)
        form2 = DirectMessage(request.POST, instance=user)

    if str(inboxcount) == "0":
        inboxcount = "0"
    if str(outboxcount) == "0":
        outboxcount = "0"
    template = "profile/profile.html"
    context = {
        "inbox": inbox,
        "inboxcount": inboxcount,
        "outbox": outbox,
        "outboxcount": outboxcount,
        "form": form1,
        "IM": form2,
        "user": user,
    }

    return render(request, template, context)
