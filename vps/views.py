import uuid

from django_filters import rest_framework as filters
from rest_framework import viewsets

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
