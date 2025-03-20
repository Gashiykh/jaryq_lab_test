from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.RedirectView.as_view(), name='redirect'),
    path('reservations', views.ReservationListView.as_view(), name='reservations'),
    path('reservations/add', views.ReservationCreateView.as_view(), name='reservations_add'),
    path('reservations/<int:id>', views.ReservationDetailView.as_view(), name='reservations_detail'),
    path('reservations/<int:id>/delete', views.ReservationDeleteView.as_view(), name='reservations_delete'),
]