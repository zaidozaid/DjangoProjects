import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

#Fake pop Script

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen =Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name = random.choice(topics))[0]
    t.save
    return t

def populate(N=2):

    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        #creating new wepage entry

        webpg = Webpage.objects.get_or_create(category=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(N=3)
    print("populating compelete!")










