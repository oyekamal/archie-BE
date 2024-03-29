# Generated by Django 4.1.7 on 2023-05-29 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0004_activity_run_gpt"),
    ]

    operations = [
        migrations.CreateModel(
            name="KeyUsage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("api_key", models.CharField(max_length=255)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                ("count", models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
