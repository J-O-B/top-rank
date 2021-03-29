from django.shortcuts import render


def index(request):
    """
    View To Return Homepage
    """
    return render(request, 'home/index.html')
