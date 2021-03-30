from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name="about_us"),
    path('fees/', views.fees, name="fees"),
    path('comission/', views.commission, name="commission"),
    path('freelance-features/', views.feat_freelancer, name="feat_freelancer"),
    path('buyer-features/', views.feat_members, name="feat_members"),
]
