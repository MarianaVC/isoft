from django.contrib import admin
from .models import (
    FacturaProducto,
    NotaCreditoProducto,
    FacturaNotaCredito,
    NotaCredito,
    Factura,
)

# Register your models here.


class FacturaProductoAdminInline(admin.TabularInline):
    model = FacturaProducto
    extra = 1


class FacturaNotaCreditoInline(admin.TabularInline):
    model = FacturaNotaCredito
    extra = 1


class FacturaAdmin(admin.ModelAdmin):
    list_display = ("no_factura", "fecha_factura", "cve_vendedor", "cve_cliente")
    inlines = [FacturaProductoAdminInline, FacturaNotaCreditoInline]


class FacturaProductoAdmin(admin.ModelAdmin):
    list_display = ("no_factura", "cve_producto", "qty", "precio", "iva")


class NotaCreditoProductoInline(admin.TabularInline):
    model = NotaCreditoProducto
    extra = 1


class NotaCreditoAdmin(admin.ModelAdmin):
    list_display = ("no_nc", "fecha_nc", "cve_vendedor", "cve_cliente")
    inlines = [NotaCreditoProductoInline]


class NotaCreditoProductoAdmin(admin.ModelAdmin):
    list_display = ("no_nc", "cve_producto", "qty")


class FacturaNotaCreditoAdmin(admin.ModelAdmin):
    list_display = ("no_nc", "cve_producto", "no_factura", "qty_dev")


admin.site.register(Factura, FacturaAdmin)
admin.site.register(NotaCredito, NotaCreditoAdmin)
# admin.site.register(NotaCreditoProducto, NotaCreditoProductoAdmin)
# admin.site.register(FacturaProducto, FacturaProductoAdmin)
# admin.site.register(FacturaNotaCredito, FacturaNotaCreditoAdmin)
