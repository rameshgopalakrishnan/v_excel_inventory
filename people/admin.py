from django.contrib import admin
from .models import MasterSection, InternalUser


@admin.register(MasterSection)
class MasterSectionAdmin(admin.ModelAdmin): pass

@admin.register(InternalUser)
class MasterInternalUserAdmin(admin.ModelAdmin): pass
