# Generated by Django 3.2.3 on 2021-06-03 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_auto_20210603_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.asociation'),
        ),
    ]
