# Generated by Django 3.0.8 on 2020-08-08 00:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fbbackend', '0012_account_session_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='session_id',
        ),
    ]