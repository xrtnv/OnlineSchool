from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, LessonList, LessonDetail

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),
]