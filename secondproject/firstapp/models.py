from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Topic(models.Model):
    topic_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    category = models.ForeignKey(Topic)
    name = models.CharField(max_length=264)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):

    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class MyUser(models.Model):
    Name = models.CharField(max_length=248)
    Email = models.EmailField(max_length=248)



    def __str__(self):
        return self.Name


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)


    portfolio = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username