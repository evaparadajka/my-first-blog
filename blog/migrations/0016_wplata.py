# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20170108_1552'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wplata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=40)),
                ('data_wplaty', models.DateField(blank=True, null=True)),
                ('kwota', models.IntegerField()),
            ],
        ),
    ]
