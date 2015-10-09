# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('author', models.CharField(default='', max_length=50)),
                ('category', models.CharField(default='', max_length=100)),
                ('Pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
