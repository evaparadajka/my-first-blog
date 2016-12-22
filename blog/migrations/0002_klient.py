# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Klient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nazwisko', models.CharField(max_length=200)),
                ('telefon', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('numerkarty', models.CharField(max_length=200)),
                ('uwagi', models.CharField(max_length=200)),
                ('styl', models.CharField(max_length=200)),
                ('instruktor', models.CharField(max_length=200)),
                ('poziom', models.CharField(max_length=200)),
                ('imie', models.CharField(max_length=200)),
                ('dzien', models.CharField(max_length=200)),
                ('wazneod', models.DateTimeField(null=True, blank=True)),
                ('waznedo', models.DateTimeField(null=True, blank=True)),
                ('ilosc', models.CharField(max_length=200)),
                ('pozostalo', models.CharField(max_length=200)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
