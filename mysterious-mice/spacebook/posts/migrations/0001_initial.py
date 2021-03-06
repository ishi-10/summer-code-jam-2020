# Generated by Django 3.0.8 on 2020-08-02 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("rovers", "0007_auto_20200801_1551"),
    ]

    operations = [
        migrations.CreateModel(
            name="ImagePost",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(upload_to="images")),
                ("description", models.TextField()),
                ("date", models.DateTimeField()),
                (
                    "rover",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="rovers.Rover"
                    ),
                ),
            ],
        ),
    ]
