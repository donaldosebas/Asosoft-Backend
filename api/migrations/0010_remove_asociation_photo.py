# Generated by Django 3.2 on 2021-05-30 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_asociation_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asociation',
            name='photo',
        ),
    ]