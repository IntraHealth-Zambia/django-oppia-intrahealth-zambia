# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-10 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oppia', '0016_auto_20180609_1723'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='course',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
