from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import BasketProduct
from .serializers import ProductInBasketSerializer


class ProductInBasketViewSet(ModelViewSet):
    serializer_class = ProductInBasketSerializer

    def get_queryset(self):
        """
        Получаем список добавленных товаров в корзину.
        """
        return BasketProduct.objects.filter(session_key=self.request.session.session_key, ordered=False)

    def list(self, request, *args, **kwargs):
        """
        При первом запросе проверяем есть ли ключ.
        """
        if not request.session.session_key:
            request.session.cycle_key()

        return super().list(request, *args, **kwargs)
