# Generated by Django 3.1 on 2020-08-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MUD', '0003_player_online'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='secret_room_connects',
            field=models.ManyToManyField(blank=True, to='MUD.Room'),
        ),
    ]
