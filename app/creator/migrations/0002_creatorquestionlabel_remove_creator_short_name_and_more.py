# Generated by Django 4.1.7 on 2023-07-12 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("creator", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="CreatorQuestionLabel",
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
                ("language", models.TextField()),
                ("number_of_students", models.TextField()),
                ("age", models.TextField()),
                ("grade", models.TextField()),
                ("course", models.TextField()),
                ("description", models.TextField()),
                ("teaching_intention", models.TextField()),
                ("learning_objectives", models.TextField()),
                ("duration", models.TextField()),
                ("educational_approach", models.TextField()),
                ("learning_approach_and_strategies", models.TextField()),
                ("desired", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="creator",
            name="short_name",
        ),
        migrations.CreateModel(
            name="CreatorQuestion",
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
                ("short_name", models.CharField(max_length=50)),
                ("question", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "creator",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.creator",
                    ),
                ),
                (
                    "creator_question_label",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="creator.creatorquestionlabel",
                    ),
                ),
            ],
        ),
    ]
