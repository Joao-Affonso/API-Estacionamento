from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vehicle.views import *

router = DefaultRouter()
router.register('vehicles/type', VehicleTypeViewSet)
router.register('vehicles', VehicleViewSet)


urlpatterns = [
    path('', include(router.urls))
    
]