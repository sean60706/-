# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=0, max_digits=4)),
                ('ingredient', models.CharField(max_length=1000)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('photo', models.CharField(max_length=1000)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=200)),
                ('operating_time', models.CharField(max_length=50)),
                ('introduction', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=200)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(to='restaurants.Restaurant'),
        ),
    ]
