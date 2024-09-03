from django.db import models
import uuid


# Create your models here.
class Producto(models.Model):
    cve_producto = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    descripcion = models.CharField(max_length=400)
    precio = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.descripcion
