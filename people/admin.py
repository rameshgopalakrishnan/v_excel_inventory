from django.contrib import admin
from .models import MasterSection, InternalUser, Customer


@admin.register(MasterSection)
class MasterSectionAdmin(admin.ModelAdmin): pass


@admin.register(InternalUser)
class InternalUserAdmin(admin.ModelAdmin): pass


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin): pass
