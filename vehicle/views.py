from rest_framework import viewsets
from vehicle.models import *
from vehicle.serializers import *
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from core.permissions import IsOwnerofVehicleOrRecord
from vehicle.filters import *


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    permission_classes = [DjangoModelPermissions, IsAdminUser]
    rql_filter_class = VehicleTypeFilterClass


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerofVehicleOrRecord]
    rql_filter_class = VehicleFilterClass

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
