# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170501_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='email',
            new_name='e_mail',
        ),
    ]
