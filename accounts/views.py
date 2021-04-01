from django.shortcuts import render


def dashboard(request):
    """
    View to return the user dashboard
    """
    return render(request, 'accounts/dashboard.html')
