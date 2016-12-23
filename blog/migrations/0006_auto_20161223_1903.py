# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20161223_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klient',
            name='uczestniczyl',
            field=models.TextField(),
        ),
    ]
