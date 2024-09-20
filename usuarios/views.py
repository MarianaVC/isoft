from rest_framework import viewsets, mixins
from .models import Vendedor
from .serilizers import VendedorListSerializer, IndicadoresSerializer
from rest_framework import permissions, viewsets
from rest_framework import generics
from datetime import datetime


class VendedorListAPIView(generics.ListAPIView):
    queryset = Vendedor.objects.all().order_by("paterno")
    serializer_class = VendedorListSerializer
    # permission_classes = [permissions.IsAuthenticated]

class AllIndicadoresListAPIView(generics.ListAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = IndicadoresSerializer

class IndicadoresListAPIView(generics.RetrieveAPIView):
    serializer_class = IndicadoresSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Vendedor.objects.all()

    # def get_serializer_context(self):
    #     mes = self.request.GET.get("mes", None)
    #     ano = self.request.GET.get("ano", None)
    #     if mes and ano:
    #         return {
    #             "month": mes,
    #             "year": ano,
    #         }
    #     return {"month": datetime.now().month, "year": datetime.now().year}
