from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics

from payments.models import Payment
from .models import CustomUser
from .serializers import PaymentSerializer, UserSerializer
from .filters import PaymentFilter


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = PaymentFilter
    ordering_fields = ['payment_date']


class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
