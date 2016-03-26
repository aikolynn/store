# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', blank=True)),
            ],
            options={
                'verbose_name': '\u5bfc\u8d2d',
                'db_table': 'employee',
                'managed': False,
                'verbose_name_plural': '\u5bfc\u8d2d',
            },
        ),
        migrations.CreateModel(
            name='InClass',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d', blank=True)),
                ('isend', models.IntegerField(null=True, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x9c\xab\xe7\xba\xa7', blank=True)),
                ('depth', models.IntegerField(null=True, verbose_name=b'\xe7\xba\xa7\xe6\x95\xb0', blank=True)),
                ('idfather', models.IntegerField(null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7ID', blank=True)),
            ],
            options={
                'verbose_name': '\u5b58\u8d27\u5206\u7c7b',
                'db_table': 'class',
                'managed': False,
                'verbose_name_plural': '\u5b58\u8d27\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='inventoryclass',
            fields=[
                ('id', models.CharField(max_length=255, serialize=False, verbose_name=b'ID', primary_key=True)),
                ('code', models.CharField(max_length=255, null=True, verbose_name=b'\xe7\xbc\x96\xe7\xa0\x81', blank=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('isendnode', models.CharField(max_length=255, null=True, verbose_name=b'\xe6\x9c\xab\xe7\xba\xa7\xe6\xa0\x87\xe8\xaf\x86', db_column=b'isEndNode', blank=True)),
                ('depth', models.CharField(max_length=255, null=True, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe7\xba\xa7\xe6\x95\xb0', blank=True)),
                ('idparent', models.CharField(max_length=255, null=True, verbose_name=b'\xe4\xb8\x8a\xe7\xba\xa7ID', blank=True)),
            ],
            options={
                'verbose_name': '\u5b58\u8d27\u5206\u7c7b',
                'db_table': 'inventoryclass',
                'managed': False,
                'verbose_name_plural': '\u5b58\u8d27\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='order_flow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inventory_code', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xad\x98\xe8\xb4\xa7\xe7\xbc\x96\xe7\xa0\x81', blank=True)),
                ('inventory_name', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\xad\x98\xe8\xb4\xa7\xe5\x90\x8d\xe7\xa7\xb0', blank=True)),
                ('quantity', models.IntegerField(null=True, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f', blank=True)),
                ('saleprice', models.FloatField(null=True, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe4\xbb\xb7', blank=True)),
                ('retailprice', models.FloatField(null=True, verbose_name=b'\xe9\x9b\xb6\xe5\x94\xae\xe4\xbb\xb7', blank=True)),
            ],
            options={
                'verbose_name': '\u9500\u552e\u6d41\u6c34',
                'db_table': 'order_flow',
                'managed': False,
                'verbose_name_plural': '\u9500\u552e\u6d41\u6c34',
            },
        ),
        migrations.CreateModel(
            name='OrderMain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_id', models.CharField(max_length=200, null=True, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe5\x8d\x95\xe5\x8f\xb7', blank=True)),
                ('order_data', models.DateField(null=True, verbose_name=b'\xe5\x8d\x95\xe6\x8d\xae\xe6\x97\xb6\xe9\x97\xb4', blank=True)),
                ('order_weekday', models.CharField(max_length=200, null=True, verbose_name=b'\xe5\x8d\x95\xe6\x8d\xae\xe6\x98\x9f\xe6\x9c\x9f', blank=True)),
                ('order_saleamount', models.FloatField(null=True, verbose_name=b'\xe5\x8d\x95\xe6\x8d\xae\xe9\x94\x80\xe5\x94\xae\xe9\x87\x91\xe9\xa2\x9d', blank=True)),
                ('order_amount', models.FloatField(null=True, verbose_name=b'\xe5\x8d\x95\xe6\x8d\xae\xe9\x9b\xb6\xe5\x94\xae\xe9\x87\x91\xe9\xa2\x9d', blank=True)),
            ],
            options={
                'verbose_name': '\u9500\u552e\u4e3b\u8868',
                'db_table': 'order_main',
                'managed': False,
                'verbose_name_plural': '\u9500\u552e\u4e3b\u8868',
            },
        ),
        migrations.CreateModel(
            name='sale_id_inventory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store', models.CharField(max_length=255, null=True, blank=True)),
                ('order_id', models.TextField(null=True, blank=True)),
                ('orderdate', models.CharField(max_length=16, null=True, blank=True)),
                ('orderweekday', models.CharField(max_length=30, null=True, blank=True)),
                ('inventory_code', models.CharField(max_length=255, null=True, db_column=b'Inventory_code', blank=True)),
                ('inventory_name', models.CharField(max_length=255, null=True, db_column=b'Inventory_name', blank=True)),
                ('unitname', models.CharField(max_length=200, null=True, blank=True)),
                ('firstclass', models.CharField(max_length=200, null=True, blank=True)),
                ('secondclass', models.CharField(max_length=200, null=True, blank=True)),
                ('thirdclass', models.CharField(max_length=200, null=True, blank=True)),
                ('quantity', models.FloatField(null=True, blank=True)),
                ('saleprice', models.FloatField(null=True, blank=True)),
                ('saleamount', models.FloatField(null=True, blank=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('retailamount', models.FloatField(null=True, db_column=b'retailAmount', blank=True)),
                ('present', models.CharField(max_length=255, null=True, blank=True)),
                ('employee', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'db_table': 'sale_id_inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='\u5e97\u94fa', blank=True)),
            ],
            options={
                'verbose_name': '\u5e97\u94fa',
                'db_table': 'store',
                'managed': False,
                'verbose_name_plural': '\u5e97\u94fa',
            },
        ),
    ]
