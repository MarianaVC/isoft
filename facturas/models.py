from django.db import models
from usuarios.models import Cliente, Vendedor
from productos.models import Producto
import uuid


# Create your models here.
class Factura(models.Model):
    no_factura = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_factura = models.DateTimeField()
    cve_vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    cve_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)


class FacturaProducto(models.Model):
    no_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    cve_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    qty = models.IntegerField(default=1)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    iva = models.DecimalField(max_digits=6, decimal_places=2)


class NotaCredito(models.Model):
    no_nc = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha_nc = models.DateTimeField()
    cve_vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    cve_cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)


class NotaCreditoProducto(models.Model):
    no_nc = models.ForeignKey(NotaCredito, on_delete=models.CASCADE)
    cve_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    qty = models.IntegerField(default=1)


class FacturaNotaCredito(models.Model):
    no_nc = models.ForeignKey(NotaCredito, on_delete=models.CASCADE)
    cve_producto = models.ForeignKey(Producto, on_delete=models.DO_NOTHING)
    no_factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    qty_dev = models.IntegerField(default=0)
