# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20151029_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'album'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
