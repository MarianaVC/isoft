from rest_framework import serializers
from .models import Vendedor
from facturas.models import (
    Factura,
    FacturaNotaCredito,
    NotaCredito,
    NotaCreditoProducto,
)
from productos.models import Producto
from zonas.models import Zona


class VendedorSerializer(serializers.ModelSerializer):
    cve_vendedor = serializers.UUIDField(read_only=True)
    nombre = serializers.CharField(read_only=True)
    paterno = serializers.CharField(read_only=True)
    materno = serializers.CharField(read_only=True)
    razon_social = serializers.CharField(read_only=True)
    # facturado_unidades = serializers.SerializerMethodField()
    # facturado_importe = serializers.SerializerMethodField()
    # devuelto_unidades = serializers.SerializerMethodField()
    # venta_neta_unidades = serializers.SerializerMethodField()
    # venta_neta_importe = serializers.SerializerMethodField()
    # comision_generada = serializers.SerializerMethodField()
    # comision_pagada = serializers.SerializerMethodField()

    class Meta:
        model = Vendedor
        fields = ("cve_vendedor", "nombre", "paterno", "materno", "razon_social")
