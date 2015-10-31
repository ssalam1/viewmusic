# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50, verbose_name=b'album', db_tablespace=b'something', db_index=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50, db_tablespace=b'indexes', db_index=True),
        ),
    ]
