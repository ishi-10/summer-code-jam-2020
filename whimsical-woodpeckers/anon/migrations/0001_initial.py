# Generated by Django 3.0.9 on 2020-08-04 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnonUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_seen', models.DateTimeField()),
            ],
        ),
    ]
