from django.contrib import admin
from .models import MasterWorkable, MasterAttribute, MasterService, MasterProduct, MasterProcess, MappingProductServicesProcess


@admin.register(MasterAttribute)
class MasterAttributeAdmin(admin.ModelAdmin): pass


@admin.register(MasterWorkable)
class MasterWorkableAdmin(admin.ModelAdmin): pass


@admin.register(MasterService)
class MasterServiceAdmin(admin.ModelAdmin): pass


@admin.register(MasterProduct)
class MasterProductAdmin(admin.ModelAdmin): pass


@admin.register(MasterProcess)
class MasterProcessAdmin(admin.ModelAdmin): pass


@admin.register(MappingProductServicesProcess)
class MappingProductServicesProcessAdmin(admin.ModelAdmin): pass
