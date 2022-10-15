from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import VPSViewSet

v1_router = DefaultRouter()
v1_router.register("vps", VPSViewSet)

urlpatterns = [
    path("v1/", include(v1_router.urls)),
]
