from django import forms
from .models import CustomMessage


class DirectMessage(forms.ModelForm):
    class Meta:
        model = CustomMessage
        exclude = (
            "sender", "created",)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)