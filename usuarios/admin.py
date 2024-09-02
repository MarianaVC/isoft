from django.contrib import admin
from .models import Cliente, Vendedor, TipoPersona

# Register your models here.
admin.site.register(TipoPersona)
admin.site.register(Vendedor)
admin.site.register(Cliente)
