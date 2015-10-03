# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20151001_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(upload_to=b'item_images')),
                ('show_in_front_page', models.BooleanField(default=True)),
                ('always_show_in_front_page', models.BooleanField(default=True)),
                ('is_trending', models.BooleanField(default=True)),
                ('category', models.ForeignKey(to='items.Category')),
            ],
        ),
    ]
