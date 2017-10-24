from django.db import models

# Create your models here.

class user(models.Model):

    firstname = models.CharField(max_length=254)
    lastname = models.CharField(max_length=245)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.firstname




