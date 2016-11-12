from rest_framework import viewsets

from people.models import Customer
from people.serializers import CustomerSerializer


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
