# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 05:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171020_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='shdsfsdf', max_length=100),
        ),
    ]
