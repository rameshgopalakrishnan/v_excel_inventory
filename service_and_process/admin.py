from django.contrib import admin
from service_and_process.models import MasterWorkable, MasterAttribute


@admin.register(MasterAttribute)
class MasterAttributeAdmin(admin.ModelAdmin): pass


@admin.register(MasterWorkable)
class MasterWorkableAdmin(admin.ModelAdmin): pass
