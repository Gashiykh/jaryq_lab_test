from django import forms

from core.models import (
    Reservation,
)


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ["table", "timeslot"]

