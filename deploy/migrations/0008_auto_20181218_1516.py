# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 07:16
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0007_auto_20181218_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jids',
            name='jid',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/TWmbReKgEa7AXJ8RrbfrYvWlWlAXRVCbv9wbhPDYmVllgdK6uWq7L7wH4cLcM8KB3hmrtHL4M9psPxDK', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]
