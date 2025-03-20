from django.db import models


class Restaurant(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Название ресторана"
    )
    address = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        verbose_name="Адрес"
    )

    def __str__(self):
        return f"Ресторан {self.name}"