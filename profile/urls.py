from django.urls import path, include
from . import views

urlpatterns = [
    path('make_update_profile/', views.MakeOrUpdate, name="MakeOrUpdate"),
    path('', views.ProfileView, name="ProfileView"),
]
