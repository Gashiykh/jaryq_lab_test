from django.views import generic

from webapp.views.reservation import (
    ReservationListView,
    ReservationDetailView,
    ReservationCreateView,
    ReservationDeleteView
)


class RedirectView(generic.RedirectView):
    pattern_name = "reservations"