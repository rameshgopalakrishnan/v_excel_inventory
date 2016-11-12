from .models import *
from rest_framework import serializers


class MasterWorkableSerializer(serializers.ModelSerializer):
    attribute = serializers.PrimaryKeyRelatedField(queryset=MasterAttribute.objects.all())

    class Meta:
        model = MasterWorkable
        fields = '__all__'
