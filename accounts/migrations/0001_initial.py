# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-29 16:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('latlong', models.CharField(max_length=30)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_menu', to='menu.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(blank=True, choices=[('restaurant', 'Restaurant'), ('waiter', 'Waiter'), ('buyer', 'Buyer')], max_length=20, null=True)),
                ('cellphone', models.CharField(blank=True, max_length=15, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='waiter_restaurant', to='accounts.Restaurant')),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waiter_user_profile', to='accounts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='buyerhistory',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_history', to='accounts.UserProfile'),
        ),
        migrations.AddField(
            model_name='buyerhistory',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_history_restaurant', to='accounts.Restaurant'),
        ),
    ]
