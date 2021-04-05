from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProfileView, name="ProfileView"),
    path('make_update_profile/', views.MakeOrUpdate, name="MakeOrUpdate"),
]
