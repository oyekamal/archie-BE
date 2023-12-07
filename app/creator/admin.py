from django.contrib import admin

from .models import (
    CreatorQuestion,
    CreatorQuestionGrouping,
    CreatorOutput,
    ConsolidatedQuestions,
)


@admin.register(CreatorQuestion)
class CreatorQuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_name",
        "question_label",
        "help_text",
        "internal_description",
        "language",
        "user_input",
        "created_at",
        "updated_at",
    )
    list_filter = ("user_input", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(CreatorQuestionGrouping)
class CreatorQuestionGroupingAdmin(admin.ModelAdmin):
    list_display = ("id", "short_name", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    # raw_id_fields = ('question',)
    date_hierarchy = "created_at"


@admin.register(CreatorOutput)
class CreatorOutputAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content",
        "label",
        "user",
        "created_at",
        "updated_at",
    )
    list_filter = ("label", "user", "created_at", "updated_at")
    date_hierarchy = "created_at"


@admin.register(ConsolidatedQuestions)
class ConsolidatedQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "short_name",
        "user",
        "questoin_group",
        "question",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "questoin_group", "created_at", "updated_at")
    date_hierarchy = "created_at"
