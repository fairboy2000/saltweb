# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-18 08:00
from __future__ import unicode_literals

import deploy.storage
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0030_auto_20181218_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='salt_event_returns',
            name='alter_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='moduleattchment',
            name='attchment',
            field=models.FileField(blank=True, null=True, storage=deploy.storage.FileStorage(), upload_to='salt/module/FmbTqYUMNBuanhJwgQgEeuryTT9vcxsVrWYqvCjwyHDCUjFSeQ7yxnTjfjewU6gfDP8AYV8Vr9vjGPCd', verbose_name='\u6a21\u5757\u4e0a\u4f20'),
        ),
    ]