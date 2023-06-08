from django.db.models import QuerySet, Avg, Count
from django_filters import NumberFilter, BooleanFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from .models import Category, Product, Review, Tag, Subcategory
from .paginations import CatalogViewSetPagination
from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, TagSerializer, BannerSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BannerViewSet(ModelViewSet):
    serializer_class = BannerSerializer

    def get_queryset(self):
        queryset = []
        for subcategory in Subcategory.objects.all():
            if subcategory.products.all():
                queryset.append(subcategory)
        return queryset[:3]


class CatalogFilter(FilterSet):
    """
    Фильтр для получения значений в диапазоне по полю price.
    """
    filter_min_price = NumberFilter(field_name="price", lookup_expr="gte")
    filter_max_price = NumberFilter(field_name="price", lookup_expr="lte")
    filter_free_delivery = BooleanFilter(field_name="free_delivery")
    category = NumberFilter(field_name="subcategory_id")

    class Meta:
        model = Product
        fields = ["price", "free_delivery"]


class CatalogViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CatalogViewSetPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = CatalogFilter
    search_fields = ['title', 'description']

    def get_ordering_queryset(self, queryset):
        """
        Возвращает отсортированный QuerySet.
        Нужно это переместить в класс, но пока как-то так.
        """
        ordering = self.request.query_params.get("ordering")
        if ordering:
            if "-" in ordering:
                direction = "-"
            else:
                direction = ""

            ordering_name = ordering.replace("-", "")

            ORDERING_NAME = ['price', 'created_at']
            ORDERING_NAME_WITH_ANNOTATE = {
                "rating": (
                    queryset.all()
                    .annotate(avg_rating=Avg("reviews__rate"))
                    .order_by(f"{direction}avg_rating")
                ),
                "reviews": (
                    queryset.all()
                    .annotate(count_reviews=Count("reviews"))
                    .order_by(f"{direction}count_reviews")
                ),
            }

            if ordering_name in ORDERING_NAME:
                return queryset.all().order_by(ordering)
            return ORDERING_NAME_WITH_ANNOTATE.get(ordering_name, queryset.all())
        return queryset.all()

    def get_queryset(self):
        # todo переделать на супер.
        """
        Стандартная функция с дополнением в получения отсортированного queryset.
        """
        assert self.queryset is not None, (
            "'%s' should either include a `queryset` attribute, "
            "or override the `get_queryset()` method."
            % self.__class__.__name__
        )
        queryset = self.queryset
        if isinstance(queryset, QuerySet):
            queryset = self.get_ordering_queryset(queryset)
        return queryset


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductLimitedViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(limited=True)


class ProductPopularViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(popular=True)


class ReviewViewSet(ModelViewSet):
    authentication_classes = []
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def create(self, request, pk=None, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        queryset_serializer = self.get_serializer(self.queryset.filter(product_id=pk), many=True)
        return Response(queryset_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
