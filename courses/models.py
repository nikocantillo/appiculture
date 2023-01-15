from django.utils import timezone
from django.db import models
from django.shortcuts import reverse

# Create your models here.

def user_thumbnail_directory_path(instance, filename):
    return 'courses/{0}/{1}'.format(instance.title, filename)

def chapter_directory_path(instance, filename):
    return 'courses/{0}/{1}/{2}'.format(instance.course, instance.title, filename)

def lesson_directory_path(instance, filename):
    return 'courses/{0}/{1}/lesson #{2}/{4}'.format(
        instance.course, 
        instance.chapter, 
        instance.lesson_number, 
        instance.title, 
        filename,
    )

class Author(models.Model):
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Course(models.Model):

    slug = models.SlugField(
        max_length=250, 
        unique_for_date="published",
        null=False,
        unique=True,
    )
    authors = models.ManyToManyField(Author)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100)
    thumbnail = models.ImageField(
        upload_to=user_thumbnail_directory_path, 
        blank=True,
        null=True
    )
    
    video = models.FileField(
        upload_to=user_thumbnail_directory_path, 
        blank=True,
        null=True,
    )
    embebe_url = models.CharField(
        max_length=200,
        null=True,
        blank=False
    )
    published = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:detail", kwargs={
            'slug': self.slug
        })


class Chapter(models.Model):

    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    chapter_number = models.IntegerField(
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=100,
    )
    thumbnail = models.ImageField(
        upload_to = chapter_directory_path,
        blank = True,
        null = True
    )
    video_chapter = models.FileField(
        upload_to = chapter_directory_path, 
        blank=True,
        null=True,
    )
    content = models.TextField(
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:chapter-detail", kwargs={
            'course_slug': self.course.slug,
            'chapter_number': self.chapter_number,
        })

class Lesson(models.Model):

    course = models.ForeignKey(
        Course, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    chapter = models.ForeignKey(
        Chapter, 
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    lesson_number = models.IntegerField(
        blank=True,
        null=True,
    )
    title = models.CharField(
        max_length=100,
    )
    thumbnail = models.ImageField(
        upload_to = lesson_directory_path,
        blank = True,
        null = True
    )
    video = models.FileField(
        upload_to=lesson_directory_path, 
        blank=True,
        null=True,
    )
    content = models.TextField(
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson-detail", kwargs={
            'course_slug': self.chapter.course.slug,
            'chapter_number': self.chapter.chapter_number,
            'lesson_number': self.lesson_number
        })

