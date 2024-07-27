from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, SubscriptionAPIView, LessonList, LessonDetail, LessonCreate, LessonUpdate, LessonDelete

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('subscribe/', SubscriptionAPIView.as_view(), name='subscribe'),
    path('lessons/', LessonList.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),
    path('lessons/create/', LessonCreate.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/update/', LessonUpdate.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDelete.as_view(), name='lesson-delete'),
]