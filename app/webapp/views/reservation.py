from django.views import generic
from django.urls import reverse, reverse_lazy

from core.models import Reservation
from webapp.forms import ReservationForm


class ReservationListView(generic.ListView):
    model = Reservation
    template_name = 'reservation/list.html'
    context_object_name = 'reservations'


class ReservationDetailView(generic.DetailView):
    model = Reservation
    template_name = 'reservation/detail.html'
    pk_url_kwarg = 'id'


class ReservationCreateView(generic.CreateView):
    models = Reservation
    template_name = 'reservation/create.html'
    form_class = ReservationForm

    def get_success_url(self):
        return reverse('reservations_detail', kwargs={'id': self.object.id})


class ReservationDeleteView(generic.DeleteView):
    model = Reservation
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy("reservations")