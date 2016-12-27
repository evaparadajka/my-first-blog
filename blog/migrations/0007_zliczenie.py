# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20161223_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zliczenie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('numerkarty', models.CharField(max_length=20)),
            ],
        ),
    ]
