from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('edit/', views.edit, name="edit"),
    path('registration/', views.register, name="register"),
]
