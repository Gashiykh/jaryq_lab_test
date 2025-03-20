from django.db import models


class Table(models.Model):
    restaurant = models.ForeignKey(
        "core.Restaurant",
        on_delete=models.CASCADE,
        related_name="tables",
        verbose_name="Ресторан"
    )
    number = models.PositiveIntegerField(
        verbose_name="Номер столика"
    )
    class Meta:
        unique_together = ("restaurant", "number")

    def __str__(self):
        return f"{self.restaurant.name} — столик №{self.number}"