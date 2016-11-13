from rest_framework import viewsets

from production_system.models import Task
from production_system.serializers import TaskSerializer

from production_system.models import Order
from production_system.models import Item
from production_system.models import Inventory
from production_system.models import Purchase
from production_system.models import Production
from production_system.models import ProductInventory
from production_system.models import MasterRawMaterial
from production_system.models import MasterTag


from production_system.serializers import OrderSerializer
from production_system.serializers import ItemSerializer
from production_system.serializers import InventorySerializer
from production_system.serializers import PurchaseSerializer
from production_system.serializers import ProductionSerializer
from production_system.serializers import ProductInventorySerializer
from production_system.serializers import RawMaterialSerializer
from production_system.serializers import TagSerializer
from production_system.serializers import InvoiceSerializer


class TaskViewset(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class InventoryViewset(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class PurchaseViewset(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer


class ProductionViewset(viewsets.ModelViewSet):
    queryset = Production.objects.all()
    serializer_class = ProductionSerializer


class ProductInventoryViewset(viewsets.ModelViewSet):
    queryset = ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer

class RawMaterialViewset(viewsets.ModelViewSet):
    queryset = MasterRawMaterial.objects.all()
    serializer_class = RawMaterialSerializer

class TagViewset(viewsets.ModelViewSet):
    queryset = MasterTag.objects.all()
    serializer_class = TagSerializer


class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Order.objects.all().prefetch_related('order_id', 'items', 'customer_id', 'tag_id', 'expected_timestamp', 'completed_timestamp')