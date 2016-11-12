from .models import *
from rest_framework import serializers


class MasterWorkableSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterWorkable
