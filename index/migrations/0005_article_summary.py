# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2018-02-06 05:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20180201_2331'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(default='2\u67082\u65e5\u5468\u4e94\u65e9\u95fb\uff0c\u5728\u5cb8\u4eba\u6c11\u5e01\u3001\u79bb\u5cb8\u4eba\u6c11\u5e01\u5151\u7f8e\u5143\u53cc\u53cc\u6da8\u78346.28\u5173\u53e3\uff0c\u5468\u4e94\u4eba\u6c11\u5e01\u4e2d\u95f4\u4ef7\u4e0a\u8c03160\u70b9\uff0c\u62a56.2885\uff0c\u7eed\u521b2015\u5e748\u670811\u65e5\u4ee5\u6765\u65b0\u9ad8\u3002', max_length=10000, verbose_name='\u6458\u8981'),
            preserve_default=False,
        ),
    ]
