# Generated by Django 4.2.6 on 2023-10-28 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("command_pusher", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="action",
            name="port",
            field=models.CharField(max_length=20),
        ),
    ]
