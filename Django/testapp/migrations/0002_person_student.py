# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('P_NO', models.IntegerField()),
                ('P_NAME', models.CharField(max_length=64)),
                ('P_Digistion', models.FloatField()),
                ('P_ADDRESS', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('S_NO', models.IntegerField()),
                ('S_NAME', models.CharField(max_length=64)),
                ('S_Class', models.FloatField()),
                ('S_ADDRESS', models.CharField(max_length=64)),
            ],
        ),
    ]
