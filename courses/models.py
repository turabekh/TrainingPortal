from django.db import models
from django.conf import settings
from autoslug import AutoSlugField
from django.urls import reverse




class Level(models.Model):
    BEGINNER = 1
    INTERMEDIATE = 2
    ADVANCED = 3

    COURSE_LEVELS = (
        (BEGINNER, "Beginner"),
        (INTERMEDIATE, "Intermediate"),
        (ADVANCED, "Advanced"),
    )

    id = models.PositiveSmallIntegerField(choices=COURSE_LEVELS, primary_key=True)

    def __str__(self):
      return self.get_id_display()

class Category(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    color = models.CharField(max_length=100, default="primary")
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Course(models.Model):
    title = models.CharField(max_length=300, null=False, unique=True)
    short_description = models.TextField(blank=True, default="")
    description = models.TextField()
    course_materials = models.CharField(max_length=500, blank=True, null=True)
    active = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='title')
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    time_to_finish = models.IntegerField(default=0)
    category = models.ForeignKey(Category,  on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class Topic(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=300, null=False, unique=True)
    description = models.TextField() 
    slug = AutoSlugField(populate_from='title', default="default-slug")
    time_to_finish = models.IntegerField(default=0)
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})


class LearningObjective(models.Model):
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
