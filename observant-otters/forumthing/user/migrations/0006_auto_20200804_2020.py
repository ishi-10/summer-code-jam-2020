# Generated by Django 3.0.8 on 2020-08-05 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20200802_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forumuser',
            name='nickname',
            field=models.TextField(default=''),
        ),
    ]
