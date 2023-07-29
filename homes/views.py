from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

class TenantViewSet(ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    

class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
class FlatViewSet(ModelViewSet):
    queryset = Flat.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddFlatSerializer
        return FlatSerializer