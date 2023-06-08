from django.db import models

from order_app.models import Order


class Payment(models.Model):
    """
    Класс оплата заказа.
    """
    order = models.ForeignKey(
        Order,
        null=True,
        on_delete=models.SET_NULL,
        related_name="payments",
        verbose_name="Заказ"
    )
    name = models.CharField(
        max_length=200,
        verbose_name='Имя владельца'
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер карты'
    )
    year = models.CharField(
        max_length=4,
        verbose_name='Год'
    )
    month = models.CharField(
        max_length=2,
        verbose_name='Месяц'
    )
    code = models.CharField(
        max_length=3,
        verbose_name='Код'
    )
    successful_payment = models.BooleanField(
        default=False
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )

    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
