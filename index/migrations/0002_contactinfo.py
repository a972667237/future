# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-01-31 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='\u8054\u7cfb\u4eba')),
                ('photo', models.CharField(max_length=11, verbose_name='\u7535\u8bdd')),
                ('qq', models.CharField(max_length=11, verbose_name='QQ')),
                ('mail', models.EmailField(max_length=254, verbose_name='\u90ae\u7bb1')),
            ],
        ),
    ]
