# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20161228_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='klient',
            name='dzien',
            field=models.CharField(max_length=20, default='sroda'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='email',
            field=models.CharField(max_length=30, default='mail@mail.pl'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='ilosc',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='imie',
            field=models.CharField(max_length=30, default='imie1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='instruktor',
            field=models.CharField(max_length=70, default='Janusz'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='nazwisko',
            field=models.CharField(max_length=40, default='nazwisko1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='numerkarty',
            field=models.CharField(max_length=20, default=1234),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='poziom',
            field=models.CharField(max_length=20, default='open'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='pozostalo',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='styl',
            field=models.CharField(max_length=20, default='taniec towarzyski'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='telefon',
            field=models.CharField(max_length=30, default='123456789'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='uczestniczyl',
            field=models.TextField(default='0'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='uwagi',
            field=models.CharField(max_length=50, default='brak'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='klient',
            name='waznedo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='klient',
            name='wazneod',
            field=models.DateField(blank=True, null=True),
        ),
    ]
