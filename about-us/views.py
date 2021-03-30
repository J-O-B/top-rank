from django.shortcuts import render


def about_us(request):
    """
    View To Return Homepage
    """
    return render(request, 'about-us/about.html')
