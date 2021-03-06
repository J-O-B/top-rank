from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class ProfileChoices():
    SKILLS = (
        ("seo", "SEO"),
        ("web", "Web Design"),
        ("content", "Content Creation"),
        ("graphic", "Graphic Design"),
        ("video", "Video Editing"),
        ("other", "Other"),
        ("none", "None"),
    )
    QUALIFICATIONS = (
        ("high_school", "High School"),
        ("university", "University"),
        ("none", "Prefer Not To Say"),
    )
    RANK = (
        (1, "Member"),
        (2, "Recruit"),
        (3, "Officer"),
        (4, "Sergeant"),
        (5, "General"),
    )
    MEMBERTYPE = (
        (1, "Member"),
        (2, "Freelancer"),
    )


class Profile(models.Model):
    class Meta:
        verbose_name_plural = "Profiles"
    """
    A profile model to allow customized user experience.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE)

    first_name = models.CharField(
        max_length=100, null=True, blank=True)

    last_name = models.CharField(
        max_length=100, null=True, blank=True)

    email = models.EmailField(
        max_length=100, null=True, blank=True)

    phone = models.CharField(
        max_length=50, null=True, blank=True)

    bio = models.TextField(null=True, blank=True)

    skill1 = models.CharField(
        max_length=9, choices=ProfileChoices.SKILLS,
        null=True, blank=True, default="none")

    skill2 = models.CharField(
        max_length=9, choices=ProfileChoices.SKILLS,
        null=True, blank=True, default="none")

    skill3 = models.CharField(
        max_length=9, choices=ProfileChoices.SKILLS,
        null=True, blank=True, default="none")

    qualification = models.CharField(
        max_length=15, choices=ProfileChoices.QUALIFICATIONS,
        null=True, blank=True, default="none")

    earnings = models.DecimalField(
        max_digits=40, decimal_places=2, null=True, blank=True, default=0)

    sales = models.IntegerField(
        null=True, blank=True, default=0)

    card_number = models.CharField(
        max_length=16, null=True, blank=True)

    orders = models.IntegerField(
        null=True, blank=True, default=0)

    products = models.CharField(
        max_length=1024, null=True, blank=True)

    product_count = models.IntegerField(
        null=True, blank=True, default=0)

    hourly_rate = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0)

    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True, default=0)

    rank = models.IntegerField(
        choices=ProfileChoices.RANK,
        null=True, blank=True, default=1)

    user_type = models.IntegerField(
        choices=ProfileChoices.MEMBERTYPE,
        null=True, blank=True, default=1)

    image_url = models.URLField(
        max_length=1024, null=True, blank=True)

    image = models.ImageField(
        null=True, blank=True)

    facebook = models.CharField(
        max_length=255, null=True, blank=True)

    linkedin = models.CharField(
        max_length=255, null=True, blank=True)

    instagram = models.CharField(
        max_length=255, null=True, blank=True)

    twitter = models.CharField(
        max_length=255, null=True, blank=True)

    personal_website = models.CharField(
        max_length=255, null=True, blank=True)

    member_since = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    try:
        if created:
            Profile.objects.create(user=instance)
        # Existing users: Just save the profile
        instance.profile.save()
    except Exception:
        instance.profile.save()

    
