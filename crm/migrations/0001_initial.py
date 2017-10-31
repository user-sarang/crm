# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 02:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data_added', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('data_added', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='lead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Lead'),
        ),
    ]
