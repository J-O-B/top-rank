from django.contrib import admin
from .models import Product, Category, SubCategory
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'subcategory',
        'i_will',
        'name',
        'created_by_id',
        'price',
        'rating',
        'sales'
    )
    ordering = ('sales',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )
    ordering = ('friendly_name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )
    ordering = ('friendly_name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)