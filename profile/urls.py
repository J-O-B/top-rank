from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.ProfileView, name="ProfileView"),
    path('after-login/', views.after_login, name="after-login"),
]
