# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 20:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserDashboard', '0004_auto_20161117_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='message',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='reciever',
        ),
        migrations.RemoveField(
            model_name='messages',
            name='user',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
