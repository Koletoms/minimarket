from basket_app.models import BasketProduct


def update_basket_past_login(old_session_key: str, new_session_key: str, user: int) -> None:
    """
    Обновляет ключ сессии и корзины на прошлой сессии.
    """
    active_basket_products: list = BasketProduct.objects.filter(session_key=old_session_key)
    last_product_in_basket = BasketProduct.objects.filter(user=user).order_by("date").last()
    last_basket_products = None
    print(user)
    print(last_product_in_basket.ordered)
    print(last_product_in_basket.date)
    print(last_product_in_basket.quantity)
    if not last_product_in_basket.ordered:
        last_basket_products = BasketProduct.objects.filter(session_key=last_product_in_basket.session_key)

    if active_basket_products.exists():
        for basket_product in active_basket_products:
            basket_product.session_key = new_session_key
            basket_product.save()

    if last_basket_products:
        for basket_product in last_basket_products:
            basket_product.session_key = new_session_key
            basket_product.save()
