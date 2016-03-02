# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ESPMCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, default='N/A')),
                ('description', models.TextField(null=True, blank=True)),
                ('image', models.ImageField(null=True, blank=True, upload_to='uploads')),
                ('starting_date', models.CharField(max_length=200, null=True, blank=True)),
                ('duration', models.CharField(max_length=200, null=True, blank=True)),
                ('price', models.CharField(max_length=50, null=True, blank=True)),
                ('location', models.CharField(max_length=200, null=True, blank=True)),
                ('category', models.CharField(max_length=50, choices=[('Gestão', 'Gestão'), ('Digital', 'Digital'), ('Marketing', 'Marketing')], null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ImageField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.ImageField(upload_to='uploads')),
                ('page', models.ForeignKey(to='lpage.CustomPage')),
            ],
        ),
        migrations.CreateModel(
            name='IntegerField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.IntegerField()),
                ('page', models.ForeignKey(to='lpage.CustomPage')),
            ],
        ),
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('page', models.ForeignKey(to='lpage.CustomPage')),
            ],
        ),
        migrations.AddField(
            model_name='charfield',
            name='page',
            field=models.ForeignKey(to='lpage.CustomPage'),
        ),
    ]
