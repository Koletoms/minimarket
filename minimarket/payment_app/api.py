from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet

from .models import Payment
from .serializers import PaymentSerializer


class PaymentViewSet(ModelViewSet):
    """
    Представление для отображение последнего незавершенного заказа.
    """
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PaymentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            if serializer.data["successful_payment"]:  # Проверяем прошел ил платеж
                return Response(status=HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        """
        Получаем значение id заказа, юзера и передаем его в сериализатор чтобы создать оплату.
        """
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field
        serializer.save(order_id=self.kwargs[lookup_url_kwarg])
