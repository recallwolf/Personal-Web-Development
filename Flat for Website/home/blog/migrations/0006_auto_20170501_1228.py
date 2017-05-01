# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170501_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='comments',
            new_name='c_omments',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='name',
            new_name='n_ame',
        ),
    ]
