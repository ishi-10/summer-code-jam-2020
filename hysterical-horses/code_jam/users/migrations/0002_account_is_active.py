# Generated by Django 3.0.8 on 2020-08-07 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
