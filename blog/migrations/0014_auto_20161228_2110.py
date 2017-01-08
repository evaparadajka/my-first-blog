# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20161228_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtr',
            name='atrybut',
            field=models.CharField(max_length=40),
        ),
    ]
