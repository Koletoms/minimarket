from django.contrib import admin

from shop_app.models import Category, Subcategory, Product, Image, Tag, Review, Specification


# class SubcategoryInline(admin.TabularInline):
#     """
#     Класс для вывода к какому заказу привязан продукт.
#     """
#     model = Category.subcategory


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Класс для категорий товаров.
    """

    list_display = "pk", "title"
    list_display_links = "pk", "title"
    search_fields = "title",


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    """
    Класс для категорий товаров.
    """

    list_display = "pk", "title", "category"
    list_display_links = "pk", "title"
    search_fields = "title",


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Класс для товаров.
    """
    list_display = "pk", "title", "subcategory"
    list_display_links = "pk", "title"
    search_fields = "title",


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    """
    Класс для фотографий товаров.
    """
    list_display = "pk", "product"
    list_display_links = "pk", "product"


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Класс для тегов продуктов товаров.
    """
    list_display = "pk", "title"
    # list_display_links = "pk", "product"#


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Класс отзывов товаров.
    """
    list_display = "pk", "product"
    list_display_links = "pk", "product"


@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    """
    Класс  товаров.
    """
    list_display = "title", "value", "product"
    list_display_links = "title",
