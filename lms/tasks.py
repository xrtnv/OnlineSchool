from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Course, Subscription


@shared_task
def send_course_update_email(course_id):
    course = Course.objects.get(id=course_id)
    subscriptions = Subscription.objects.filter(course=course)
    for subscription in subscriptions:
        send_mail(
            'Course Update Notification',
            f'The course "{course.title}" has been updated.',
            settings.DEFAULT_FROM_EMAIL,
            [subscription.user.email],
        )
