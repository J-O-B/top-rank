from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SubCategory(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)

    sub_category = models.ForeignKey(
        'SubCategory', null=True, blank=True, on_delete=models.SET_NULL)

    i_will = models.CharField(
        max_length=254)

    name = models.CharField(
        max_length=254)

    description = models.TextField()

    price = models.DecimalField(
        max_digits=6, decimal_places=2)

    rating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True)

    image_url = models.URLField(
        max_length=1024, null=True, blank=True)

    image = models.ImageField(
        null=True, blank=True)

    created_by = models.CharField(
        max_length=254)

    time_to_complete = models.DecimalField(
        max_digits=6, decimal_places=1, null=False, blank=False)

    tags = models.CharField(
        max_length=254, blank=True, null=True)

    def __str__(self):
        return self.name
