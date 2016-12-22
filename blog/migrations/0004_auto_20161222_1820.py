# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20161222_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='ilosc',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='pozostalo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
