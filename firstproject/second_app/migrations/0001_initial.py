# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=245)),
                ('lastname', models.CharField(max_length=245)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
