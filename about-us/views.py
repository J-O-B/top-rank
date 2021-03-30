from django.shortcuts import render


def about_us(request):
    """
    View to return the general about page
    """
    return render(request, 'about-us/about.html')


def fees(request):
    """
    View to return the pricing page within about app
    """
    return render(request, 'about-us/fees.html')


def commission(request):
    """
    View to return the pricing page within about app
    """
    return render(request, 'about-us/commission.html')


def feat_freelancer(request):
    """
    View to return the pricing page within about app
    """
    return render(request, 'about-us/freelancer.html')


def feat_members(request):
    """
    View to return the pricing page within about app
    """
    return render(request, 'about-us/members.html')
