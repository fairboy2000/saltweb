# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 07:30
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0019_auto_20181218_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/JFSYhH9CTT4cgJAuByYaxedlXHtYAQ98pMcJDLlDScYd6eXx6GxlLcHPbLHtDPLSw8gan7YkCRyjQJgU', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
        migrations.AlterIndexTogether(
            name='salt_event_returns',
            index_together=set([]),
        ),
    ]