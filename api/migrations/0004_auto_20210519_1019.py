# Generated by Django 3.2 on 2021-05-19 16:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210519_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='category',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='tournament',
            name='country',
            field=models.CharField(default='Guatemala', max_length=32),
        ),
        migrations.AddField(
            model_name='tournament',
            name='current_date',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tournament',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tournament',
            name='total_dates',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tournament',
            name='tournament_logo',
            field=models.URLField(default=''),
        ),
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biography', models.TextField(blank=True, max_length=200)),
                ('wins', models.IntegerField(default=0)),
                ('loses', models.IntegerField(default=0)),
                ('games', models.IntegerField(default=0)),
                ('contact', models.CharField(blank=True, max_length=200)),
                ('asociation', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.asociation')),
            ],
        ),
    ]
