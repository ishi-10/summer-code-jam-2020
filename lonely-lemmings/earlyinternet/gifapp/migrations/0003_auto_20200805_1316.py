# Generated by Django 3.0.9 on 2020-08-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifapp', '0002_auto_20200805_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project_type',
        ),
        migrations.AddField(
            model_name='project',
            name='is_gif',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='ProjectType',
        ),
    ]