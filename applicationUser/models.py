from django.db import models
from cuser.models import AbstractCUser
from django.conf import settings
from PIL import Image


class User(AbstractCUser):
    pass

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(default="", blank=True)
    image = models.ImageField(default="default.jpg", upload_to="profile_pics")

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
