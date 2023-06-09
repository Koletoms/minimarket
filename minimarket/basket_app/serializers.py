from rest_framework import serializers

from shop_app.models import Product, Image
from .models import BasketProduct


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]


class ProductInBasketSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField(source="product.id", required=False)
    title = serializers.CharField(source="product.title", max_length=100, read_only=True)
    description = serializers.CharField(source="product.description", max_length=400, read_only=True)
    href = serializers.SerializerMethodField()
    images = ImageSerializer(source="product.images", many=True, required=False)

    class Meta:
        model = BasketProduct
        fields = ["id", "product_id", "title", "fixed_price", "description", "quantity", "href",  "images"]
        read_only_fields = ["id", "title", "fixed_price", "description"]

    def create(self, validated_data):
        """
        Создает товара или добавляет количество в корзину.
        """
        request = self.context.get("request")
        if not request.session.session_key:
            request.session.cycle_key()
        session_key = request.session.session_key
        product_id = validated_data["product"]["id"]
        quantity = validated_data["quantity"]
        product = Product.objects.get(id=product_id)
        basket_product = BasketProduct.objects.filter(session_key=session_key, product_id=product_id)
        user = None
        if request.user.is_authenticated:
            user = request.user

        if basket_product.exists():
            basket_product = basket_product[0]
            basket_product.quantity += quantity
            basket_product.save()
            return basket_product

        return BasketProduct.objects.create(
            user=user,
            session_key=session_key,
            product_id=product_id,
            quantity=quantity,
            fixed_price=product.price
        )

    def update(self, instance, validated_data):
        instance.quantity += validated_data["quantity"]
        instance.save()
        return instance

    def get_href(self, product):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/product/{product.product.pk}")
