from django.contrib import admin
from .models import Zona


class ZonaAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "cve_zona")
    search_fields = ("descripcion",)


admin.site.register(Zona, ZonaAdmin)
