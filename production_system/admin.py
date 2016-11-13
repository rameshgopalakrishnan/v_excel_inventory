from django.contrib import admin
from .models import MasterTag, Order, Item, MasterRawMaterial, Inventory, Purchase, MappingProductMaterial, Task, Production, ProductInventory


@admin.register(MasterTag)
class MasterTagAdmin(admin.ModelAdmin): pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin): pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin): pass

@admin.register(MasterRawMaterial)
class MasterRawMaterialAdmin(admin.ModelAdmin): pass

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin): pass

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin): pass

@admin.register(MappingProductMaterial)
class MappingProductMaterialAdmin(admin.ModelAdmin): pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin): pass

@admin.register(Production)
class ProductionAdmin(admin.ModelAdmin): pass

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin): pass
