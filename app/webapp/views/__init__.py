from django.views import generic

from webapp.views.reservation import (
    SeatingChartView
)


class RedirectView(generic.RedirectView):
    pattern_name = "reservation_chart"