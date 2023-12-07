from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    private = models.BooleanField(default=False)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    ai_answer = models.BooleanField(default=False)
    run_gpt = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("activity:activity_list")


class KeyUsage(models.Model):
    api_key = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.PositiveIntegerField(default=0)

    def increment(self):
        self.count += 1
        self.save()

    def reset(self):
        self.count = 0
        self.save()

    def __str__(self):
        return f"{self.api_key} - {self.count}"
