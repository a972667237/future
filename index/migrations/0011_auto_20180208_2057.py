# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-08 12:57
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_friend_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpage_article',
            name='article',
            field=DjangoUeditor.models.UEditorField(verbose_name='\u5185\u5bb9'),
        ),
    ]
