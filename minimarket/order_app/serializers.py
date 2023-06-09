from rest_framework import serializers

from shop_app.models import Product, Image
from .models import Order, OrderProduct, Delivery
from basket_app.models import BasketProduct


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        exclude = ["available"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]


class OrderProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    product_id = serializers.CharField(source="product.id", max_length=100)
    category = serializers.CharField(source="product.subcategory.id", max_length=100, read_only=True)
    date = serializers.DateTimeField(read_only=True)
    title = serializers.CharField(source="product", read_only=True)
    description = serializers.CharField(source="product.description", read_only=True)
    freeDelivery = serializers.BooleanField(source="product.free_delivery", read_only=True)
    tags = serializers.ListField(source="product.get_id_tags", read_only=True)
    reviews = serializers.IntegerField(source="product.get_count_reviews", read_only=True)
    rating = serializers.FloatField(source="product.get_rating", read_only=True)
    href = serializers.SerializerMethodField(read_only=True)
    images = ImageSerializer(source="product.images", many=True, required=False, read_only=True)

    class Meta:
        model = OrderProduct
        fields = ["category", "id", "product_id", "fixed_price", "quantity", "date", "title", "description",
                  "rating", "freeDelivery", "images", "tags", "href", "reviews"]

    def get_href(self, order_product):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/product/{order_product.product.id}")


class OrderSerializer(serializers.ModelSerializer):
    orderId = serializers.CharField(source="id", max_length=100, read_only=True)
    createdAt = serializers.CharField(source="created", max_length=100, required=False)
    deliveryType = serializers.CharField(source="delivery_type", required=False)
    deliveryPrice = serializers.DecimalField(source="delivery_price", max_digits=10, decimal_places=2, required=False)
    paymentType = serializers.CharField(source="payment_type", required=False)
    fullName = serializers.CharField(max_length=200, required=False)
    email = serializers.CharField(max_length=100, required=False)
    phone = serializers.CharField(max_length=20, required=False)
    totalCost = serializers.DecimalField(source="get_total_cost", max_digits=10, decimal_places=2, read_only=True)
    products = OrderProductSerializer(source="order_products", many=True)

    class Meta:
        model = Order
        fields = ["orderId", "createdAt", "fullName", "email", "phone", "deliveryType", "deliveryPrice", "paymentType",
                  "totalCost", "status", "city", "address", "products"]

    def create(self, validated_data):
        """
        Создает Заказ и переносит в него продукты из корзины.
        """
        products = validated_data.pop('order_products')
        user = validated_data.pop('user')
        session_key = validated_data.pop('session_key')
        order = Order.objects.create(
            fullName=user.username,
            user=user,
            phone=user.profile.phone_number,
            email=user.email
        )
        for product in products:
            OrderProduct.objects.create(
                order=order,
                product_id=product["product"]["id"],
                fixed_price=product["fixed_price"],
                quantity=product["quantity"]
            )

        last_cart = BasketProduct.objects.filter(session_key=session_key)
        if last_cart.exists():
            for cart_product in last_cart:
                cart_product.ordered = True
                cart_product.save()
        return order

    def update(self, instance, validated_data):
        """
        Йня какая-то, надо бы переписать.
        """
        instance.fullName = validated_data.get('fullName', instance.fullName)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.email = validated_data.get('email', instance.email)
        instance.delivery_type = validated_data.get('delivery_type', instance.delivery_type)
        instance.delivery_price = validated_data.get('delivery_price', instance.delivery_price)
        instance.payment_type = validated_data.get('payment_type', instance.payment_type)
        instance.city = validated_data.get('city', instance.city)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
