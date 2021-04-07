from django import forms
from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _
from .models import Profile


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = (
        'custom_widget_templates/custom_clearable_file_input.html')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = (
            "user", "earnings", "rating",
            "sales", "products", "rank",
            "image_url")
    image = forms.ImageField(
        label='image', required=False, widget=ClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
