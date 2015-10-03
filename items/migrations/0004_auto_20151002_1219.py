# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 12, 18, 42, 511310, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 2, 12, 19, 10, 527623, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
