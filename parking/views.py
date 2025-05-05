from rest_framework import viewsets
from parking.models import *
from parking.serializers import *
from rest_framework.permissions import DjangoModelPermissions
from core.permissions import IsOwnerofVehicleOrRecord
from parking.filters import *


class ParkingSpotViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpot.objects.all()
    serializer_class = ParkingSpotSerializer
    permission_classes = [DjangoModelPermissions]
    rql_filter_class = ParkingSpotFilterClass
    
    
class ParkingRecordViewSet(viewsets.ModelViewSet):
    queryset = ParkingRecord.objects.all()
    serializer_class = ParkingRecordSerializer
    permission_classes = [DjangoModelPermissions, IsOwnerofVehicleOrRecord]
    rql_filter_class = ParkingRecordFilterClass
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return ParkingRecord.objects.all()
        return ParkingRecord.objects.filter(vehicle__owner__user=user)