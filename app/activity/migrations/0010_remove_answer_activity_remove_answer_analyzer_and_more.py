# Generated by Django 4.2.2 on 2023-11-25 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0009_alter_activity_options_alter_analyzer_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='analyzer',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questioninanalyzer',
            name='analyzer',
        ),
        migrations.RemoveField(
            model_name='questioninanalyzer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='analyzer',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='analyzer_language',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='file',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_universal',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='language',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='url',
        ),
        migrations.DeleteModel(
            name='Analyzer',
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='QuestionInAnalyzer',
        ),
    ]