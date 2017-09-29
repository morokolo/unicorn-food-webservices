# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-29 12:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyerhistory',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_history', to='accounts.UserProfile'),
        ),
        migrations.AlterField(
            model_name='buyerhistory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_history_restaurant', to='accounts.Restaurant'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cellphone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to='Media'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='restaurant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='waiter_restaurant', to='accounts.Restaurant'),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiter_user_profile', to='accounts.UserProfile'),
        ),
    ]
