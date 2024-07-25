from django.contrib.contenttypes.models import ContentType
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User, Permission, Group
from .models import Course, Lesson, Subscription


class LessonCRUDTests(APITestCase):
    def setUp(self):
        content_type = ContentType.objects.get_for_model(Lesson)
        create_lesson_permission = Permission.objects.create(
            codename='can_create_lesson',
            name='Can create lesson',
            content_type=content_type,
        )
        delete_lesson_permission = Permission.objects.create(
            codename='can_delete_lesson',
            name='Can delete lesson',
            content_type=content_type,
        )

        self.user = User.objects.create_user(username='user', email='user@user.user', password='pass')
        self.moderator = User.objects.create_user(username='mod', email='mod@user.user', password='pass', is_staff=True)
        self.moderator.user_permissions.add(create_lesson_permission)
        self.moderator.user_permissions.add(delete_lesson_permission)
        self.course = Course.objects.create(title='Test Course')
        self.lesson = Lesson.objects.create(title='Test Lesson', course=self.course)
        self.moderator.groups.create(name='Модераторы')
        group = Group.objects.get(name='Модераторы')
        self.moderator.groups.add(group)

    def test_create_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse('lesson-list')
        with open('C:\\Users\\elliot\\PycharmProjects\\DRF\\lms\\lessons\\previews\\defImage.jpg', 'rb') as img:
            image_content = img.read()

        image = SimpleUploadedFile(name='defImage.jpg',
                                   content=image_content,
                                   content_type='image/jpeg')

        data = {
            'title': 'New Lesson',
            'course': self.course.id,
            'description': 'A detailed description of the new lesson.',
            'video_url': 'https://www.youtube.com/watch?v=C2tUSHnhoSc',
            'preview_image': image
        }

        response = self.client.post(url, data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse('lesson-detail', kwargs={'pk': self.lesson.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_update_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse('lesson-detail', kwargs={'pk': self.lesson.id})

        data = {
            'title': 'New Lesson',
            'course': self.course.id,
            'description': 'A detailed description of the new lesson.',
            'video_url': 'https://www.youtube.com/watch?v=C2tUSHnhoSc',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        self.client.force_authenticate(user=self.moderator)
        url = reverse('lesson-detail', kwargs={'pk': self.lesson.id})
        response = self.client.delete(url)

        # Отладочная информация
        if response.status_code != status.HTTP_204_NO_CONTENT:
            print("Права пользователя:", self.moderator.user_permissions.all())
            print("Группы пользователя:", self.moderator.groups.all())
            print("Response Status Code:", response.status_code)
            print("Response Content:", response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user', email='user@user.user', password='pass')
        self.course = Course.objects.create(title='Test Course')

    def test_subscribe_to_course(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('subscribe')
        data = {'course_id': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('Подписка добавлена', response.data['message'])

    def test_unsubscribe_from_course(self):
        self.client.force_authenticate(user=self.user)
        Subscription.objects.create(user=self.user, course=self.course)
