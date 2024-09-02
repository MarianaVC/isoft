from django.contrib import admin
from .models import FacturaProducto, NotaCreditoProducto, FacturaNotaCredito

# Register your models here.
admin.site.register(FacturaProducto)
admin.site.register(NotaCreditoProducto)
admin.site.register(FacturaNotaCredito)
