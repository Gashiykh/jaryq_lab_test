from django.views.generic import ListView

from core.models import Table, Reservation


class SeatingChartView(ListView):
    model = Table
    template_name = "reservation/chart.html"
    context_object_name = "tables"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            timeslot = int(self.request.GET.get("timeslot", 12))
        except ValueError:
            timeslot = 12
        context["selected_timeslot"] = timeslot

        reservations = Reservation.objects.filter(timeslot=timeslot)

        reserved_table_ids = []
        for res in reservations:
            reserved_table_ids.append(res.table.id)

        context["reserved_table_ids"] = reserved_table_ids

        context["timeslot_options"] = range(0, 24)
        return context
