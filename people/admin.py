from django.contrib import admin
from .models import MasterSection


@admin.register(MasterSection)
class MasterSectionAdmin(admin.ModelAdmin): pass
