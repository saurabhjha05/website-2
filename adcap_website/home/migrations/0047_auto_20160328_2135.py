# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0046_auto_20160328_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalservicessettings',
            name='mailchimp_id',
            field=models.CharField(blank=True, help_text='Your MailChimp List ID', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='externalservicessettings',
            name='mailchimp_u',
            field=models.CharField(blank=True, help_text='Your MailChimp user ID', max_length=255, null=True),
        ),
    ]
