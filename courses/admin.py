from django.contrib import admin
from .models import Course, Chapter, Lesson, Author
# Register your models here.

admin.site.register(Author)
admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Lesson)