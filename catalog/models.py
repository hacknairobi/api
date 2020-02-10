from django.db import models


# Create your models here.
class Skill(models.Model):
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class Lesson(models.Model):
    key = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField()


class Course(models.Model):
    key = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    banner_image = models.URLField()
    featured = models.BooleanField()
    short_summary = models.CharField(max_length=200)
    required_knowledge = models.TextField()
    syllabus = models.TextField()
    homepage = models.URLField()
    summary = models.TextField()
    faq = models.TextField()
    level = models.CharField(max_length=50)
    expected_duration_unit = models.CharField(max_length=50)
    expected_duration = models.IntegerField()
    lessons = models.ManyToManyField(Lesson)


class Track(models.Model):
    key = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    level = models.CharField(max_length=50)
    description = models.TextField()
    short_description = models.TextField()
    display_title = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course)
    skills = models.ManyToManyField(Skill)
