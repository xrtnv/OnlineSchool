from django.contrib import admin

from lms.models import Lesson, Course

admin.site.register(Course)
admin.site.register(Lesson)
