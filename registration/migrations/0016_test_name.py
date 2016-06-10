# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20160610_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='name',
            field=models.CharField(default=1, max_length=25, verbose_name='Test name'),
            preserve_default=False,
        ),
    ]
