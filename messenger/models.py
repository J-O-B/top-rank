from django.db import models
from django.contrib.auth.models import User


class CustomMessage(models.Model):
    class Meta:
        verbose_name_plural = "Messages"

    sender = models.ForeignKey(
        User, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(
        User, related_name="reciever", on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender)

    def get_reciever(self):
        return str(self.reciever)

    def get_created(self):
        return str(self.created)

