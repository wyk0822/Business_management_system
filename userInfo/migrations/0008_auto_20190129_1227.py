# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-29 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0007_auto_20190128_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='goods_jifen',
            field=models.DecimalField(decimal_places=2, default=100.0, max_digits=7, verbose_name='兑换所需积分'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='20190129122732728418', max_length=50, verbose_name='订单编号'),
        ),
    ]