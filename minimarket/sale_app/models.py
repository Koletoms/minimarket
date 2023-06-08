from django.db import models


class SaleProduct(models.Model):
    """
    Класс Товар в корзине.
    Необходим для обозначения условий и новой цены.
    """
    product = models.ForeignKey(
        "shop_app.Product",
        on_delete=models.CASCADE,
        related_name="sales",
        verbose_name="Product"
    )
    # discount
