from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

import datetime

now = datetime.datetime.now()
user = models.OneToOneField(User, on_delete=models.CASCADE)


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    class Meta:
        verbose_name_plural = "Sub Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    subcategory = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)
    i_will = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    skill1 = models.CharField(max_length=254, null=False, blank=False)
    skill2 = models.CharField(max_length=254, null=True, blank=True)
    skill3 = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    sales = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True)

    def __str__(self):
        return self.name
