# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20161227_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='ilosc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='pozostalo',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='uczestniczyl',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
