# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-19 04:41
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0035_auto_20181219_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salt_event_returns',
            old_name='fun_args',
            new_name='fun_args1',
        ),
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/JbRxB7p9YVBXTehqdlfhDTf3jaqy3KpTJbwd3r7e3vYeSet6tG9ALE5tw8kfvCGrdKrbHPx7B5R7DTRF', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]