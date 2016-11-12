from rest_framework import viewsets, routers
from .models import MasterWorkable
from .serializers import MasterWorkableSerializer


class MasterWorkableViewset(viewsets.ModelViewSet):
    queryset = MasterWorkable.objects.all()
    serializer_class = MasterWorkableSerializer
