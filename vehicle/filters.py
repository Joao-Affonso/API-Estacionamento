from dj_rql.filter_cls import AutoRQLFilterClass
from vehicle.models import *

class VehicleTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType
    
class VehicleFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle