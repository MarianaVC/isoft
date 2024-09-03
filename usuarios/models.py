from django.db import models
from zonas.models import Zona
import uuid

# Create your models here.


class TipoPersona(models.Model):
    cve_tipo_persona = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    descripcion = models.CharField(max_length=400, default="")

    def __str__(self):
        return self.descripcion


class Persona(models.Model):
    cve_tipo_persona = models.ForeignKey(TipoPersona, on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=400, default="")
    paterno = models.CharField(max_length=400, default="")
    materno = models.CharField(max_length=400, default="")
    razon_social = models.CharField(max_length=400)


class Vendedor(Persona):
    cve_vendedor = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    cve_zona = models.ForeignKey(Zona, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre + " " + self.paterno + " " + self.materno


class Cliente(Persona):
    cve_cliente = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.nombre + " " + self.paterno + " " + self.materno
