from django.db import models
import uuid

# Create your models here.


class Zona(models.Model):
    cve_zona = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        return self.descripcion
