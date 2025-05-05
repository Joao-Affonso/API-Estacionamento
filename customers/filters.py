from dj_rql.filter_cls import AutoRQLFilterClass
from customers.models import *

class CustomerFilterClass(AutoRQLFilterClass):
    MODEL = Customer