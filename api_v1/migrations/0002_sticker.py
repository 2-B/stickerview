# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-12 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='stickers')),
                ('tags', models.ManyToManyField(blank=True, to='api_v1.Tag')),
            ],
        ),
    ]
