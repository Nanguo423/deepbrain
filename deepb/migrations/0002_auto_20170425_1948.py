# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-25 23:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deepb', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='main_table',
            old_name='take_name',
            new_name='task_name',
        ),
    ]
