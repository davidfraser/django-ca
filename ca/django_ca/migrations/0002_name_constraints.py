# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_ca.utils

class Migration(migrations.Migration):

    dependencies = [
        ('django_ca', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificateauthority',
            name='permitted_dns',
            field=models.TextField(blank=True, help_text='Comma-separated list of domains which this CA is permitted to act as an authority for.',
                                   null=True, verbose_name='Permitted DNS for Name Constraints'),
            ),
    ]

