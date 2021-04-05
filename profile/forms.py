from django import forms
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            "user", "earnings", "rating",
            "sales", "products", "rank",
            "image_url")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)