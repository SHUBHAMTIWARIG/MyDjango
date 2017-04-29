from django.db import models
from django.utils import timezone
class creator(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=False, blank=True)
    password = models.CharField(max_length=15)
    contact = models.IntegerField(null=True, blank=True)
    option = (
        ('py', 'PYTHON DJANGO'), ('J', 'core java'), ('AJ', 'Advance java'), ('Asp', 'visual stdio'), ('cpp', 'oops'))
    field = models.CharField(default="python", max_length=12, choices=option)

    age = models.IntegerField(default=20)
    profile_image = models.ImageField(upload_to="profile")

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


# Create your models here.
