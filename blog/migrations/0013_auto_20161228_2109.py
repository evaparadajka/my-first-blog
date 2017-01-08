# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_filtr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filtr',
            name='atrybut',
            field=models.TextField(),
        ),
    ]
