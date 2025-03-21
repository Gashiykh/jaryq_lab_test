from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.RedirectView.as_view(), name='redirect'),
    path('seating/', views.SeatingChartView.as_view(), name='reservation_chart'),
]