# Generated by Django 4.1.7 on 2023-08-05 05:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("activity", "0007_rename_is_private_activity_private"),
    ]

    operations = [
        migrations.RenameField(
            model_name="activity",
            old_name="description",
            new_name="content",
        ),
    ]
