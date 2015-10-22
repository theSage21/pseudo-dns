# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mapper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('poweron', models.BooleanField(default=False)),
                ('ip', models.GenericIPAddressField()),
                ('pass_hash', models.CharField(default='None', max_length=100)),
                ('stamp', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
