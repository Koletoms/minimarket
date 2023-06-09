from basket_app.models import BasketProduct


def update_basket_past_login(old_session_key: str, new_session_key: str, user: int) -> None:
    """
    Обновляет ключ сессии и корзины на прошлой сессии.
    """
    active_basket_products: list = BasketProduct.objects.filter(session_key=old_session_key)
    old_products_in_basket = BasketProduct.objects.filter(user=user)
    all_last_products_in_basket = None

    if old_products_in_basket.exists():
        last_product_in_basket = old_products_in_basket.order_by("date").last()
        if not last_product_in_basket.ordered:
            all_last_products_in_basket = BasketProduct.objects.filter(session_key=last_product_in_basket.session_key)

    if active_basket_products.exists():
        for basket_product in active_basket_products:
            basket_product.session_key = new_session_key
            basket_product.save()

    if all_last_products_in_basket:
        for basket_product in all_last_products_in_basket:
            basket_product.session_key = new_session_key
            basket_product.save()
