# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=250)),
                ('post_date', models.DateTimeField(verbose_name='date published')),
                ('post_body', models.TextField()),
                ('post_author', models.CharField(default='Nermin Kekic', max_length=250)),
            ],
        ),
    ]
