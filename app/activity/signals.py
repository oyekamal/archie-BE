from django.db.models.signals import post_save
from django.dispatch import receiver
from django_q.tasks import async_task
from .models import Activity


def hook_funcs(task):
    print("Openai Answer are done..!")


@receiver(post_save, sender=Activity)
def activity_saved(sender, instance, **kwargs):
    print("signals-=------!")
    # ai_assistant(instance)
