from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from shop_app.models import Product

User = get_user_model()


class BasketProduct(models.Model):
    """
    Класс Товар в корзине.
    """
    session_key = models.CharField(
        max_length=200
    )
    user = models.ForeignKey(
        User,
        null=True,
        related_name='user',
        on_delete=models.SET_NULL,
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="basket_products",
        verbose_name="Product"
    )
    quantity: int = models.PositiveIntegerField(
        verbose_name="Quantity"
    )
    fixed_price: float = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(limit_value=0)],
        verbose_name="fixed price"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )
    ordered = models.BooleanField(
        default=False,
        verbose_name="Ordered"
    )

    def get_total_price(self):
        return self.quantity * self.fixed_price
