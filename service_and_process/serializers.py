from .models import *
from rest_framework import serializers

from service_and_process.models import MasterService
from service_and_process.models import MasterProduct
from service_and_process.models import MasterProcess
from service_and_process.models import MappingProductServicesProcess
from service_and_process.models import MasterWorkable


class MasterWorkableSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=MasterAttribute.objects.all())

    class Meta:
        model = MasterWorkable
        fields = '__all__'


class MasterServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterService
        fields = "__all__"


class MasterProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProduct
        fields = "__all__"


class MasterProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProcess
        fields = "__all__"

class MappingProductServicesProcessSerializer(serializers.ModelSerializer):

    class Meta:
        model = MappingProductServicesProcess
        fields = "__all__"
