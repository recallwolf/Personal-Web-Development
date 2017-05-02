# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='tip1',
        ),
        migrations.AddField(
            model_name='article',
            name='tip2',
            field=models.TextField(null=True),
        ),
    ]
