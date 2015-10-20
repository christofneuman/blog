# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151019_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactme',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 5, 27, 15, 559958, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactme',
            name='sent_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contactme',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 20, 5, 27, 27, 225865, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
