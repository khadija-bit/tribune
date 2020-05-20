# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-05-20 07:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=datetime.datetime(2020, 5, 20, 7, 18, 46, 517570, tzinfo=utc), upload_to='articles/'),
            preserve_default=False,
        ),
    ]
