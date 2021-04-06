from django.contrib import admin
from .models import CustomMessage


class CustomMessageAdmin(admin.ModelAdmin):
    list_display = (
        'sender',
        'reciever',
        'created',
    )
    ordering = ('reciever',)

admin.site.register(CustomMessage, CustomMessageAdmin)
