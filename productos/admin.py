from django.contrib import admin
from .models import Producto

# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ("descripcion", "cve_producto")
    search_fields = ("descripcion",)


admin.site.register(Producto, ProductoAdmin)
