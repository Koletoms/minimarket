from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from rest_framework.reverse import reverse

from .models import Category, Product, Review, Specification, Tag, Subcategory


class SubcategorySerializer(serializers.ModelSerializer):
    href = serializers.SerializerMethodField(read_only=True)

    def get_href(self, subcategory):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/catalog/{subcategory.pk}")

    class Meta:
        model = Category
        fields = ["id", "title", "href"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "image", "subcategories"]
        # depth = 1


class BannerSerializer(serializers.ModelSerializer):
    href = serializers.SerializerMethodField(read_only=True)
    image = serializers.ImageField()
    price = serializers.IntegerField(source="get_min_price_product")

    class Meta:
        model = Subcategory
        fields = ["id", "title", "href", "image", "price"]

    def get_href(self, subcategory):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/catalog/{subcategory.pk}")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "title"]


class ReviewSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Review
        fields = ["author", "email", "text", "rate", "date"]

    def create(self, validated_data):
        request = self.context.get("request")
        pk = request.resolver_match.kwargs['pk']
        return Review.objects.create(product_id=pk, **validated_data)


class SpecificationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="title")

    class Meta:
        model = Specification
        fields = ["name", "value"]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source="subcategory.id", max_length=100)
    date = serializers.CharField(source="created_at", max_length=100)
    fullDescription = serializers.CharField(source="description", max_length=100)
    freeDelivery = serializers.BooleanField(source="free_delivery")
    reviews = ReviewSerializer(many=True)
    href = serializers.SerializerMethodField(read_only=True)
    specifications = SpecificationSerializer(many=True)
    tags = serializers.StringRelatedField(many=True, read_only=True)
    rating = serializers.FloatField(source="get_rating", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "category", "price", "available_quantity", "date", "href", "title", "description",
                  "fullDescription", "freeDelivery", "images", "reviews", "specifications", "rating", "tags"]
        depth = 1

    def get_href(self, product):
        request = self.context.get("request")
        return request.build_absolute_uri(f"/product/{product.pk}")
