from rest_framework import serializers

from production_system.models import Task
from production_system.models import Order
from production_system.models import Item
from production_system.models import Inventory
from production_system.models import Purchase
from production_system.models import Production
from production_system.models import ProductInventory

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'


class PurchaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Purchase
        fields = '__all__'


class ProductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Production
        fields = '__all__'

class ProductInventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInventory
        fields = '__all__'

