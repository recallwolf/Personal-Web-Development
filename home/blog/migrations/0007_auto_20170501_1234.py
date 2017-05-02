# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170501_1228'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='c_omments',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='e_mail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='n_ame',
            new_name='name',
        ),
    ]
