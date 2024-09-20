from rest_framework import serializers
from datetime import datetime
from django.db.models import Sum
from .models import Vendedor
from facturas.models import (
    Factura,
    NotaCredito,
)
from zonas.models import Zona


class VendedorListSerializer(serializers.ModelSerializer):
    cveVendedor = serializers.UUIDField(source='cve_vendedor',read_only=True)
    nombre = serializers.CharField(read_only=True)
    paterno = serializers.CharField(read_only=True)
    materno = serializers.CharField(read_only=True)
    razonSocial = serializers.CharField(source='razon_social',read_only=True)
    zona = serializers.CharField(source='cve_zona',read_only=True)

    class Meta:
        model = Vendedor
        fields = ("cveVendedor", "nombre", "paterno", "materno", "razonSocial", "zona")


class IndicadoresSerializer(serializers.ModelSerializer):
    cveVendedor = serializers.UUIDField(source='cve_vendedor',read_only=True)
    nombre = serializers.CharField(read_only=True)
    paterno = serializers.CharField(read_only=True)
    materno = serializers.CharField(read_only=True)
    indicadores = serializers.SerializerMethodField(read_only=True)

    def get_facturas(self, obj, month, year):
        facturas = Factura.objects.filter(
            cve_vendedor=obj,
            fecha_factura__month=month,
            fecha_factura__year=year,
        ).select_related("facturaproducto")

        notas = NotaCredito.objects.filter(
            cve_vendedor=obj,
            fecha_nc__month=month,
            fecha_nc__year=year,
        ).select_related("facturanotacredito")

        devuelto_qty = notas.aggregate(Sum("facturanotacredito__qty_dev")).get(
            "facturanotacredito__qty_dev__sum"
        )

        devuelto_importe = notas.aggregate(
            Sum("facturanotacredito__cve_producto__precio")
        ).get("facturanotacredito__cve_producto__precio__sum")

        facturado_unidades = facturas.aggregate(Sum("facturaproducto__qty")).get(
            "facturaproducto__qty__sum"
        )
        facturado_importe = facturas.aggregate(Sum("facturaproducto__precio")).get(
            "facturaproducto__precio__sum"
        )
        facturado_unidades = facturado_unidades if facturado_unidades else 0

        facturado_importe = facturado_importe if facturado_importe else 0

        devuelto_qty = devuelto_qty if devuelto_qty else 0
        devuelto_importe = devuelto_importe if devuelto_importe else 0

        return {
            "facturadoUnidades": facturado_unidades,
            "facturadoImporte": facturado_importe,
            "devueltoUnidades": devuelto_qty,
            "devueltoImporte": devuelto_importe,
            "ventaNetaUnidades": facturado_unidades - devuelto_qty,
            "ventaNetaImporte": facturado_importe - devuelto_importe,
            "mes": month,
            "ano": year,
        }

    def range_inclusive(self, start, end):
        return range(start, end + 1)

    def get_indicadores(self, obj):
        indicadores = []
        # get first venta ever from one vendedor.
        first_factura = (
            Factura.objects.filter(cve_vendedor=obj).order_by("fecha_factura").first()
        )
        last_factura = (
            Factura.objects.filter(cve_vendedor=obj).order_by("fecha_factura").last()
        )

        if first_factura:
            first_factura = first_factura.fecha_factura
            first_month = first_factura.month
            this_year = datetime.today().year
            for i in self.range_inclusive(first_factura.year, this_year):
                if first_factura.year == last_factura.fecha_factura.year:
                    for j in self.range_inclusive(
                        first_month, last_factura.fecha_factura.month
                    ):
                        indicadores.append(self.get_facturas(obj=obj, month=j, year=i))
                else:
                    for j in self.range_inclusive(first_month, 12):
                        indicadores.append(self.get_facturas(obj=obj, month=j, year=i))

                    for k in self.range_inclusive(1, 12):
                        indicadores.append(
                            self.get_facturas(obj=obj, month=k, year=this_year)
                        )

        return indicadores

    class Meta:
        model = Vendedor
        fields = (
            "cveVendedor",
            "nombre",
            "paterno",
            "materno",
            "indicadores",
        )
