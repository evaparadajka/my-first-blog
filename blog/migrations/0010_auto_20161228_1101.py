# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20161227_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='klient',
            name='dzien',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='email',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='ilosc',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='imie',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='instruktor',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='nazwisko',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='numerkarty',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='poziom',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='pozostalo',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='styl',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='telefon',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='uczestniczyl',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='uwagi',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='waznedo',
        ),
        migrations.RemoveField(
            model_name='klient',
            name='wazneod',
        ),
    ]
