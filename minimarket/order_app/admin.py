from django.contrib import admin

from order_app.models import Delivery


@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    """
    Класс для установки вариантов доставки.
    """

    list_display = ["name_delivery"]
    list_display_links = ["name_delivery"]
