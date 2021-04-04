from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    """
    View To Return Homepage
    """
    template = 'home/index.html'
    queryset = User.objects.all()
    name = "name"
    context = {
        'queryset': queryset,
        'name': name,
    }

    return render(request, template, context)
