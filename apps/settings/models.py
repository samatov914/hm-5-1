from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name='Название'
    )
    descriptions = models.TextField(
        verbose_name= "Описание"
    )
    logo = models.ImageField(
        upload_to="logo",
        verbose_name="Логотип"
    )
    phone = models.CharField(
        max_length=100,
        verbose_name="Номер телефона"
    )
    email = models.EmailField(
        verbose_name="Email"
    )
    locate = models.CharField(
        max_length=255,
        verbose_name="Адрес"
    )
    facebook = models.URLField(
        verbose_name="Facebook"
    )
    instagram = models.URLField(
        verbose_name="Instagram"
    )
    youtube = models.URLField(
        verbose_name="Youtube"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"