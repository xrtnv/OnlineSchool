from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from users.permissions import IsModerator
from .models import Course, Lesson
from .permissions import IsOwner
from .serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsModerator]
        else:
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return [permission() for permission in permission_classes]


class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), (IsModerator() or IsOwner())]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'list', 'retrieve']:
            permission_classes = [IsAuthenticated, IsModerator]
        else:
            permission_classes = [IsAuthenticated, DjangoModelPermissions]
        return [permission() for permission in permission_classes]


class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [IsAuthenticated(), (IsModerator() or IsOwner())]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
