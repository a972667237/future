# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-07 07:26
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20180207_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinPage_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topInfo', DjangoUeditor.models.UEditorField(max_length=50000, verbose_name='\u9876\u90e8\u4fe1\u606f')),
                ('bottomInfo', DjangoUeditor.models.UEditorField(max_length=50000, verbose_name='\u5e95\u90e8\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u52a0\u5165\u6211\u4eec\u9875\u9762\u4fe1\u606f',
                'verbose_name_plural': '\u52a0\u5165\u6211\u4eec\u9875\u9762\u4fe1\u606f',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.IntegerField(choices=[(0, '\u9875\u9762\u5185\u5bb9'), (1, '\u7814\u7a76\u8d44\u8baf'), (2, '\u57fa\u7840\u77e5\u8bc6'), (3, '\u4e1a\u52a1\u6307\u5357')], default=1, verbose_name='\u6587\u7ae0\u7c7b\u578b'),
        ),
    ]
