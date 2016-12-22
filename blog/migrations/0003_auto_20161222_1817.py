# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_klient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klient',
            name='ilosc',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='pozostalo',
        ),
        migrations.AlterField(
            model_name='klient',
            name='waznedo',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='klient',
            name='wazneod',
            field=models.DateField(null=True, blank=True),
        ),
    ]
