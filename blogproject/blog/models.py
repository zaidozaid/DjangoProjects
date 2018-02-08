from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


# Create your models here

class Post(models.Model):

    author = models.ForeignKey(User)
    title = models.CharField(max_length=234)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    publish_date = models.DateField(null=True,blank=True)



    def publish(self):

        self.publish_date= timezone.now()
        self.save()

    def approve_coments(self):
        return self.comments.f



