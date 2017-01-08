# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_zliczenie'),
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
        migrations.RemoveField(
            model_name='klient',
            name='uczestniczyl',
        ),
    ]
