# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20161222_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='uczestniczyl',
            field=models.CharField(max_length=1000, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='klient',
            name='dzien',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='klient',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='klient',
            name='imie',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='klient',
            name='instruktor',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='klient',
            name='nazwisko',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='klient',
            name='numerkarty',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='klient',
            name='poziom',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='klient',
            name='styl',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='klient',
            name='telefon',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='klient',
            name='uwagi',
            field=models.CharField(max_length=50),
        ),
    ]
