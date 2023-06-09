from django.contrib.auth import get_user_model
from django.db import models

from shop_app.models import Product

User = get_user_model()


class Order(models.Model):
    PAYMENT_CHOICES = (
        ("1", "Онлайн картой"),
        ("2", "При получении"),
    )

    user = models.ForeignKey(
        User,
        null=True,
        related_name='orders',
        on_delete=models.SET_NULL,
        verbose_name='Пользователь'
    )
    fullName = models.CharField(
        max_length=200,
        verbose_name='ФИО'
    )
    email = models.EmailField(
        max_length=100,
        verbose_name='Email'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    address = models.CharField(
        blank=False,
        null=True,
        default=None,
        max_length=250,
        verbose_name='Адрес'
    )
    city = models.CharField(
        blank=False,
        null=True,
        default=None,
        max_length=100,
        verbose_name='Город'
    )
    delivery_type = models.CharField(
        max_length=30,
        verbose_name='Тип доставки',
        default="ordinary"
    )
    delivery_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена доставки',
        default=0
    )
    payment_type = models.CharField(
        max_length=30,
        choices=PAYMENT_CHOICES,
        verbose_name='Тип оплаты',
        default="1"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создан'
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Изменен'
    )
    # card_number = models.PositiveIntegerField(
    #     # validators=[MinValueValidator(10000000), MaxValueValidator(99999999)],  # Переписать
    #     blank=False,
    #     null=True,
    #     default=None,
    #     verbose_name='Номер карты'
    # )
    status = models.CharField(
        blank=False,
        null=True,
        default=None,
        max_length=150,
        verbose_name='Статус платежа'
    )

    class Meta:
        ordering = ['-created']
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f'Заказ #{self.id}'

    def get_total_cost(self):
        return round((sum(item.fixed_price * item.quantity for item in self.order_products.all())), 1)


class OrderProduct(models.Model):
    order = models.ForeignKey(
        Order,
        related_name="order_products",
        on_delete=models.CASCADE,
        verbose_name='Заказ'
    )
    product = models.ForeignKey(
        Product,
        null=True,
        related_name="order_products",
        on_delete=models.CASCADE,
        verbose_name="Товар"
    )
    fixed_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    def get_cost(self):
        return self.fixed_price * self.quantity

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"


class Delivery(models.Model):
    """
    Доступные варинты доставки.
    """
    name_delivery = models.CharField(
        max_length=100,
        verbose_name="Название",
        default="Стандартная"
    )
    type_delivery = models.CharField(
        max_length=100,
        verbose_name="Тип доставки",
        default="ordinary"

    )
    price_delivery = models.IntegerField(
        verbose_name='Цена доставки',
        default=200
    )
    limit = models.IntegerField(
        verbose_name='Граница общей стоимости',
        default=2000
    )
    above_price_limit = models.IntegerField(
        verbose_name='Цена выше границы',
        default=0
    )
    available = models.BooleanField(
        verbose_name='Доступность',
        default=True
    )

    class Meta:
        verbose_name = "Delivery"
        verbose_name_plural = "Delivery"

    def __str__(self):
        return self.name_delivery

