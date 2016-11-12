from django.contrib import admin
from .models import MasterTag


@admin.register(MasterTag)
class MasterTagAdmin(admin.ModelAdmin): pass
