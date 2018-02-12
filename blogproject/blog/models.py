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

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk':self.pk})



    def __str__(self):

        return self.title




class Comment(models.Model):
    post = models.ForeignObject('blog.Post',related_name='comments')
    author = models.CharField(max_length=254)
    text = models.TextField()
    create_date = models.DateField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)


    def approve(self):
        self.approved_comment = True
        self.save()



    def get_absolute_url(self):
        return reverse("post_list")


    def __str__(self):
        return self.text












