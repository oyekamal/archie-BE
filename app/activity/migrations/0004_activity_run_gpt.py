# Generated by Django 4.1.7 on 2023-05-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0003_activity_url_alter_activity_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="run_gpt",
            field=models.BooleanField(default=False),
        ),
    ]
