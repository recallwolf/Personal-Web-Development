# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='comment',
            new_name='comments',
        ),
    ]
