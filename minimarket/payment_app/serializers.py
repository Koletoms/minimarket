from rest_framework import serializers

from order_app.models import Order
from .models import Payment
from .services import check_payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        exclude = ["order"]

    def create(self, validated_data):
        """
        Создает Заказ и переносит в него продукты из корзины.
        """
        order_id = validated_data.pop('order_id')
        status = check_payment(validated_data.get('number'))
        payment = Payment.objects.create(order_id=order_id, successful_payment=status, **validated_data)
        if status:
            order = Order.objects.get(id=order_id)
            order.status = "Оплачен"
            order.save()
        return payment
