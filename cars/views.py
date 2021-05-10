from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cars.models import Car
from cars.permission import IsOwnerOrReadOnly
from cars.serializer import CarDetailSerializer, CarListSerializer


# Создание экземпляров
class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer
    permission_classes = [IsAuthenticated, ]


# Просмотр экземпляров
class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = [IsAuthenticated, ]


# Создание/удаление одного обьекта
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    permission_classes = [IsOwnerOrReadOnly, IsAdminUser]
