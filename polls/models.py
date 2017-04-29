from django.db import models
from django.utils import timezone


# Create your models here.
class post(models.Model):
    author = models.ForeignKey('auth.user')
    text = models.CharField(max_length=360)
    created = models.DateTimeField(default=timezone.now())
    pub_date = models.DateTimeField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def publish(self):
        self.pub_date = timezone.now()
        self.save()

    def __str__(self):
        return self.text


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%y/%m/%d')

    # store a file in media documents /2017/3/30
    def upload(self):
        self.save()

    def __str__(self):
        return self.docfile.path



