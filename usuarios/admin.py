from django.contrib import admin
from .models import Cliente, Vendedor, TipoPersona

# Register your models here.


class TipoPersonaAdmin(admin.ModelAdmin):
    list_display = ("cve_tipo_persona", "descripcion")
    search_fields = ("descripcion",)


class VendedorAdmin(admin.ModelAdmin):
    list_display = (
        "cve_tipo_persona",
        "nombre",
        "paterno",
        "materno",
        "razon_social",
        "cve_vendedor",
        "cve_zona",
    )
    search_fields = ("nombre", "paterno", "materno", "razon_social", "cve_vendedor")


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "cve_tipo_persona",
        "cve_cliente",
        "nombre",
        "paterno",
        "materno",
        "razon_social",
    )
    search_fields = ("nombre", "paterno", "materno", "razon_social", "cve_vendedor")


admin.site.register(TipoPersona, TipoPersonaAdmin)
admin.site.register(Vendedor, VendedorAdmin)
admin.site.register(Cliente, ClienteAdmin)
