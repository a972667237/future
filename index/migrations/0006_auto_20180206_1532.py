# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-06 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='join_form',
            name='place',
            field=models.CharField(default='szu', max_length=10000, verbose_name='\u5730\u5740'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.IntegerField(choices=[(0, '\u9875\u9762\u5185\u5bb9'), (1, '\u7814\u7a76\u8d44\u8baf'), (2, '\u57fa\u7840\u77e5\u8bc6')], default=1, verbose_name='\u6587\u7ae0\u7c7b\u578b'),
        ),
    ]
