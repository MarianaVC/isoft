from rest_framework import viewsets
from .models import Vendedor
from .serilizers import VendedorSerializer
from rest_framework import permissions, viewsets
from rest_framework import generics


class VendedorListAPIView(generics.ListAPIView):
    queryset = Vendedor.objects.all().order_by("paterno")
    serializer_class = VendedorSerializer
    permission_classes = [permissions.IsAuthenticated]
