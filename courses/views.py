from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import View
from .models import Course, Chapter, Lesson
from django.shortcuts import get_object_or_404, render
from authentication.utils.redirect_page import RedirectPage

# Create your views here.
class CourseDetailView(View):
    def get(self, request, slug,*args, **kwargs):
        course = get_object_or_404(Course, slug=slug)
        user = request.user.id
        if user is not None:
            context={
                'course':course
            }
            return render(request, 'courses/pages/course/details.html', context)
        return redirect('users:login')

class ChapterDetailView(LoginRequiredMixin ,View):

    def get(self, request, course_slug, chapter_number,*args, **kwargs):
        
        course = get_object_or_404(Course, slug=course_slug)


        chapter_qs = Chapter.objects.filter(course__slug=course_slug).filter(chapter_number=chapter_number)
        chapter = chapter_qs[0]

       

        context={
            'chapter':chapter,
        }

        return render(request, 'courses/pages/chapter/detail.html', context)


class LessonDetailView(LoginRequiredMixin ,View):
    
    def get(self, request, course_slug, chapter_number, lesson_number,*args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)

        
        chapter_qs = Chapter.objects.filter(course__slug=course_slug).filter(chapter_number=chapter_number)
        chapter = chapter_qs[0]

        lesson_qs = Lesson.objects \
            .filter(chapter__course__slug=course_slug) \
            .filter(chapter__chapter_number=chapter_number) \
            .filter(lesson_number=lesson_number)
        lesson = lesson_qs[0]

        context={
            'chapter':chapter,
            'lesson':lesson
        }
       
        return render(request, 'courses/pages/lesson/detail.html', context)
