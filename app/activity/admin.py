from django.contrib import admin

from .models import Activity, KeyUsage


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'summary',
        'created_at',
        'updated_at',
        'private',
        'owner',
        'ai_answer',
        'run_gpt',
    )
    list_filter = (
        'created_at',
        'updated_at',
        'private',
        'owner',
        'ai_answer',
        'run_gpt',
    )
    date_hierarchy = 'created_at'


@admin.register(KeyUsage)
class KeyUsageAdmin(admin.ModelAdmin):
    list_display = ('id', 'api_key', 'timestamp', 'count')
    list_filter = ('timestamp',)