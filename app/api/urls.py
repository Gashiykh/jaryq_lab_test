from django.urls import path

from api import views
urlpatterns = [
    path('reservations/', views.ReservationListView.as_view(), name='reservations_list'),
    path('reservations/<int:id>/', views.ReservationDetailView.as_view(), name='reservations_detail'),
    path('reservations/create/', views.ReservationCreateView.as_view(), name='reservations_create'),
    path('reservations/delete/<int:id>/', views.ReservationDeleteView.as_view(), name='reservations_delete'),
]

