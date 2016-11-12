from rest_framework import viewsets

from people.models import Customer
from people.models import InternalUser
from people.serializers import CustomerSerializer
from people.serializers import InternalUserSerializer


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class InternalUserViewset(viewsets.ModelViewSet):
    queryset = InternalUser.objects.all()
    serializer_class = InternalUserSerializer
