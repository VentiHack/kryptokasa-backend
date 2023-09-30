# Generated by Django 4.2 on 2023-09-30 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                ("name", models.CharField(max_length=255, verbose_name="Nazwa aktywa")),
                (
                    "ticker",
                    models.CharField(
                        max_length=255,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Ticker",
                    ),
                ),
                (
                    "img_url",
                    models.CharField(max_length=255, verbose_name="URL obrazka"),
                ),
            ],
            options={"verbose_name": "Aktywo", "verbose_name_plural": "Aktywa",},
        ),
    ]
