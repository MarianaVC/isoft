from django.urls import include, path
from rest_framework import routers

from usuarios import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", views.VendedorListAPIView.as_view(), name="vendedor"),
    path("indicadores/", views.AllIndicadoresListAPIView.as_view(), name="indicadores"),
    path("<pk>/", views.IndicadoresListAPIView.as_view()),

]
urlpatterns += router.urls
