from rest_framework import serializers

from people.models import Customer
from people.models import InternalUser

class CustomerSerializer(serializers.ModelSerializer):
    phone_number = serializers.IntegerField(validators=[lambda x: len(str(x)) == 10])

    class Meta:
        model = Customer
        fields = '__all__'

class InternalUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternalUser
        fields = '__all__'

