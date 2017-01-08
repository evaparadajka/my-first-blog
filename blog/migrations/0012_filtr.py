# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20161228_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtr',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('atrybut', models.CharField(max_length=40)),
            ],
        ),
    ]
