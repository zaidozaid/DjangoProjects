import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

#Fake pop Script

import random
from second_app.models import user
from faker import Faker



fakegen = Faker()

def populate(N=3):

    for entry in range(N):

        fs = fakegen.first_name()
        ls = fakegen.last_name()
        em = fakegen.email()

        users = user.objects.get_or_create(firstname=fs, lastname=ls, email=em)[0]



if __name__ == '__main__':
    print("Populating Script")
    populate(N=30)
    print("populating compelete!")







