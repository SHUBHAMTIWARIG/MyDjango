from django.db import models
from django.urls import reverse
from django.utils import timezone


# Create your models here.

class Giveaway(models.Model):
    name = models.ForeignKey("auth.User")
    giveaway_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    file = models.FileField(upload_to='documents/%y/%m/%d', null=False)
    screen_shot1 = models.ImageField(upload_to='document/%y/%m/%d', null=False)
    screen_shot2 = models.ImageField(upload_to='document/%y/%m/%d', null=False)
    screen_shot3 = models.ImageField(upload_to='document/%y/%m/%d', null=False)
    website_link = models.CharField(max_length=256, null=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return reverse("giveaway", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("giveaway_delete", kwargs={"id": self.id})
