# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-02 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='photos/')),
                ('name', models.CharField(max_length=6000)),
                ('location', models.CharField(max_length=6000)),
                ('count', models.CharField(max_length=6000)),
                ('calls', models.CharField(max_length=6000)),
            ],
        ),
    ]
