from statistics import mean

from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse

from minimarket import settings

User = get_user_model()


class Category(models.Model):
    """
    Класс категории разделов.
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    image = models.ImageField(
        upload_to='images/category/',
        default='images/default/category_default.png',
        blank=True,
        verbose_name="Image",
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))]
    )

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Subcategory(models.Model):
    """
    Класс раздел товаров.
    """
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Category"
    )
    image = models.ImageField(
        upload_to='images/subcategory/',
        default='images/default/subcategory_default.png',
        blank=True,
        verbose_name="Image",
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))]
    )

    class Meta:
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return self.title

    def get_min_price_product(self) -> float:
        x = self.products.all()
        if x.count() != 0:
            minimm = 20000000
            for product in x:
                if product.price < minimm:
                    minimm=product.price
            return minimm
            # return min(x, key=lambda product: product.price)
        return 0.0


class Product(models.Model):
    """
    Класс товара для магазина.
    """
    subcategory = models.ForeignKey(
        Subcategory,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Subcategory"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="Title"
    )
    available_quantity = models.PositiveIntegerField(
        default=1,
        verbose_name="Quantity"
    )
    description = models.TextField(
        null=False,
        blank=True,
        verbose_name="Description"
    )
    free_delivery = models.BooleanField(
        default=False
    )
    limited = models.BooleanField(
        default=False
    )
    popular = models.BooleanField(
        default=False
    )
    price = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2,
        verbose_name="Price"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    archived = models.BooleanField(
        default=False
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.title

    def get_rating(self) -> float:
        try:
            return round(mean(review.rate for review in self.reviews.all()), 1)
        except:
            return 0

    def get_id_tags(self) -> list[int]:
        return [tag.id for tag in self.tags.all()]

    def get_count_reviews(self) -> int:  # заменить на  count
        return len(self.reviews.all())


class Image(models.Model):
    """
    Класс изображение для товара.
    """
    image = models.ImageField(
        upload_to='images/products/',
        default='images/default/product_default.png',
        blank=True,
        verbose_name="Image",
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))]
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="Product"
    )


class Review(models.Model):
    """
    Класс отзыв для товара.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Product"
    )
    author = models.CharField(
        null=False,
        max_length=100,
        verbose_name="Author"
    )
    email = models.EmailField(
        null=False,
        max_length=100,
        verbose_name="Email"
    )
    text = models.TextField(
        null=False,
        blank=True,
        verbose_name="Text"
    )
    rate = models.PositiveIntegerField(
        null=False,
        verbose_name="rate"
    )
    date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class Specification(models.Model):
    """
    Класс дополнения для товаров.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="specifications",
        verbose_name="Product"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="title"
    )
    value = models.CharField(
        max_length=100,
        verbose_name="Value"
    )

    class Meta:
        verbose_name = "Specification"
        verbose_name_plural = "Specifications"


class Tag(models.Model):
    """
    Класс тегов для товаров.
    """
    product = models.ManyToManyField(
        Product,
        related_name="tags",
        verbose_name="Product"
    )
    title = models.CharField(
        max_length=100,
        verbose_name="title"
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title


class ViewedProduct(models.Model):
    """
    Класс посмотренных товаров пользователем.
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="viewed_products",
        verbose_name="Product"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="viewed_products",
        verbose_name="User"
    )
    amount_views = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        verbose_name = "ViewedProduct"
        verbose_name_plural = "ViewedProducts"
