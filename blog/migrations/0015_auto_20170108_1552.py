# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20161228_2110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filtr',
            old_name='atrybut',
            new_name='nazwisko',
        ),
        migrations.AddField(
            model_name='filtr',
            name='dzien',
            field=models.CharField(max_length=20, default='dzien'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtr',
            name='imie',
            field=models.CharField(max_length=30, default='imie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtr',
            name='instruktor',
            field=models.CharField(max_length=70, default='instruktor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtr',
            name='poziom',
            field=models.CharField(max_length=20, default='poziom'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='filtr',
            name='styl',
            field=models.CharField(max_length=20, default='styl'),
            preserve_default=False,
        ),
    ]
