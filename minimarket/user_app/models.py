from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models


User = get_user_model()


class Profile(models.Model):
    """
    Класс расширения стандартного пользователя.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="user"
    )
    phone_number = models.CharField(
        max_length=17,
        blank=True,
        verbose_name="Phone number",
        validators=[RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Необходимый формат телефона: '+79991112233'")]
    )
    avatar = models.ImageField(
        upload_to='images/avatars/',
        default='images/default/avatar_default.png',
        blank=True,
        verbose_name="Avatar",
        validators=[FileExtensionValidator(allowed_extensions=("png", "jpg", "jpeg"))]
    )

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
