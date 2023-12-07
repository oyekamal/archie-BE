from django.db import models
from django.contrib.auth.models import User


LANGUAGES = (
    ("en", "English"),
    ("fr", "French"),
    ("es", "Spanish"),
    # Add any other languages you need here
)


class CreatorQuestion(models.Model):
    short_name = models.CharField(max_length=255, default="short name")
    question_label = models.TextField(null=True)
    help_text = models.TextField(null=True, blank=True)
    internal_description = models.TextField(null=True, blank=True)
    language_choices = [
        ("en", "English"),
        ("fr", "French"),
        ("es", "Spanish"),
    ]
    language = models.CharField(
        max_length=2, choices=language_choices, default="en", null=True
    )
    user_input = models.BooleanField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.short_name

    def save(self, *args, **kwargs):
        # Check each field for '<variable>' value
        fields = [f for f in self._meta.fields if isinstance(f, (models.TextField))]
        for field in fields:
            if field.attname == "question_label":
                value = getattr(self, field.name)
                if "<variable>" not in value:  # Check if '<variable>' is in value
                    # Update the field value and append '<variable>'
                    setattr(self, field.name, value + "<variable>")
        super().save(*args, **kwargs)


class CreatorQuestionGrouping(models.Model):
    short_name = models.CharField(max_length=255, default="short name")
    question = models.ManyToManyField(CreatorQuestion, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name


class CreatorOutput(models.Model):
    content = models.TextField()
    label = models.ForeignKey(CreatorQuestion, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ConsolidatedQuestions(models.Model):
    """
    this model is responsable for storing Question created by above tables. and use for creating activity.
    """

    short_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    questoin_group = models.ForeignKey(
        CreatorQuestionGrouping, null=True, blank=True, on_delete=models.SET_NULL
    )
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.short_name
