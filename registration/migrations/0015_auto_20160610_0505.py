# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_auto_20160609_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateField(verbose_name='Test Date')),
                ('type', models.CharField(max_length=20, verbose_name='Test Type', choices=[(b'Technical', 'Technical'), (b'HR', 'HR'), (b'Quantitative', 'Quantitative'), (b'Verbals', 'Verbals'), (b'Reasoning', 'Reasoning'), (b'Eligibility', 'Eligibility'), (b'Aptitude', 'Aptitude')])),
            ],
        ),
        migrations.AlterField(
            model_name='student',
            name='branch',
            field=models.CharField(max_length=32, choices=[(b'cse', 'CSE'), (b'me', 'ME'), (b'ece', 'ECE'), (b'eee', 'EEE'), (b'csa', 'CSA')], null=True, verbose_name='Branch', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')]),
        ),
    ]
