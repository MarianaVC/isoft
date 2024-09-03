from django.urls import include, path
from rest_framework import routers

from usuarios import views

router = routers.DefaultRouter()

urlpatterns = [
    path("", views.VendedorListAPIView.as_view(), name="vendedor"),
]
urlpatterns += router.urls
