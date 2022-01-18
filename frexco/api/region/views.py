from rest_framework import viewsets
from .models import Region
from .serializers import RegionSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all().order_by('name')
    serializer_class = RegionSerializer
# Create your views here.