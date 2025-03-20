from django.db import models

from core.validators import hour_range

class Reservation(models.Model):

    table = models.ForeignKey(
        "core.Table",
        on_delete=models.CASCADE,
        related_name="reservations",
        verbose_name="Столик"
    )

    timeslot = models.PositiveIntegerField(
        verbose_name="Час бронирования",
        help_text="Введите значение от 0 до 23",
        validators=[hour_range]
    )


    class Meta:
        unique_together = ('table', 'timeslot')
        ordering = ('table', 'timeslot')

    def __str__(self):
        return f"Бронь: {self.table} на {self.timeslot}:00"