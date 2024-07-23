from django.db import models
from django.conf import settings


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview_image = models.ImageField(upload_to='courses/previews/')
    description = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='courses', null=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='lessons/previews/')
    video_url = models.URLField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lessons', null=True)

    def __str__(self):
        return self.title
