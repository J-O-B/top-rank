from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        verbose_name_plural = "Profiles"
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    bio = models.TextField()


    def __str__(self):
        return self.user
