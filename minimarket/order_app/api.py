from django.contrib.auth import logout
from django.contrib.auth.models import AnonymousUser
from django.db.models import QuerySet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import Order, Delivery
from .serializers import OrderSerializer, DeliverySerializer


class DeliveryViewSet(ModelViewSet):
    """
    Представление для вывода доступных способов доставки.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = DeliverySerializer
    pagination_class = None

    def get_queryset(self) -> QuerySet[Order]:
        """
        Возвращает список доступный видов доставки.
        """
        return Delivery.objects.filter(available=True)


class OrderActiveViewSet(ModelViewSet):
    """
    Представление для отображение последнего незавершенного заказа.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = Order.objects.filter(user=self.request.user).first()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OrderViewSet(ModelViewSet):
    """
    Представление для создания или изменения заказа. А также для получения списка заказов.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self) -> QuerySet[Order]:
        """
        Возвращает список заказов пользователя.
        """
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, session_key=self.request.session.session_key)
