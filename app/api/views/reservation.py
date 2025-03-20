from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from api.serializers import ReservationSerializer
from core.models import Reservation


class ReservationListView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)


class ReservationDetailView(APIView):
    def get(self, request, id):
        reservation = get_object_or_404(Reservation, id=id)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data)


class ReservationCreateView(APIView):
    @swagger_auto_schema(
        request_body=ReservationSerializer,
        responses={201: ReservationSerializer}
    )
    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReservationDeleteView(APIView):
    def delete(self, request, id):
        reservation = get_object_or_404(Reservation, id=id)
        reservation.delete()
        return Response(
            {"message": "Бронь удалена"},
            status=status.HTTP_204_NO_CONTENT
        )