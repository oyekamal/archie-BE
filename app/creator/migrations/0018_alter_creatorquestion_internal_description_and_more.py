# Generated by Django 4.2.2 on 2023-12-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("creator", "0017_remove_consolidatedquestions_creator_request_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creatorquestion",
            name="internal_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="creatorquestion",
            name="user_input",
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
