# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_hero_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Pub_date',
            new_name='pub_date',
        ),
    ]
