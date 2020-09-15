from django.db import models
from django.conf import settings
from courses.models import Course, Topic
from autoslug import AutoSlugField
from django.urls import reverse

class StepType(models.Model):
    VIDEO = 1
    TEXT = 2
    QUIZ = 3

    STEP_TYPE_CHOICES = (
        (VIDEO, "Video"),
        (TEXT, "Text"),
        (QUIZ, "Quiz"),
    )

    id = models.PositiveSmallIntegerField(choices=STEP_TYPE_CHOICES, primary_key=True)

    def __str__(self):
      return self.get_id_display()

class Step(models.Model):
    order = models.IntegerField(default=0)
    step_type = models.ForeignKey(StepType, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    video_url = models.URLField(default="", blank=True)
    teacher_notes = models.TextField(blank=True, default="")
    lesson_materials = models.TextField(blank=True, default="")
    content = models.TextField(default="", blank=True)
    slug = AutoSlugField(populate_from='title')
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Lesson: {self.title} - Topic: {self.topic.title}"

    def get_absolute_url(self):
        return reverse('step_detail', kwargs={'slug': self.slug})

class Assignment(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Assignment: {self.title} - Topic: {self.topic.title}"