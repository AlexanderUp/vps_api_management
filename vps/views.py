import uuid

from django.shortcuts import get_list_or_404, get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import VPSFilter
from .models import VPS
from .serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = VPSFilter

    def perform_create(self, serializer):
        while True:
            new_uuid = uuid.uuid4()
            if VPS.objects.filter(uuid=new_uuid).exists():
                continue
            break
        serializer.save(uuid=new_uuid)

    @action(methods=["post"], detail=False, url_path="get-vps-by-uuid")
    def get_vps_by_uuid(self, request):
        instance_uuid = request.data.get("uuid")
        vps_instance = get_object_or_404(VPS, uuid=instance_uuid)
        serializer = self.get_serializer(vps_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["post"], detail=False, url_path="change-status")
    def change_status(self, request):
        vps_instance = get_object_or_404(
            VPS, uuid=request.data.get("uuid"),
        )
        vps_instance.status = request.data.get("status")
        vps_instance.save()
        serializer = self.get_serializer(vps_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False, url_path="get-best-vps")
    def get_best_vps(self, request):
        vps_instances = get_list_or_404(
            VPS, cpu__gte=8, ram__gte=8, hdd__gte=128
        )
        serializer = self.get_serializer(vps_instances, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
