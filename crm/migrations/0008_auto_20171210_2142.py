# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 03:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_remove_comment_lead'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='data_added',
            new_name='date_added',
        ),
    ]
