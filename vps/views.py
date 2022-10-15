import uuid

from rest_framework import viewsets

from .models import VPS
from .serializers import VPSSerializer


class VPSViewSet(viewsets.ModelViewSet):
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer

    def perform_create(self, serializer):
        while True:
            new_uuid = uuid.uuid4()
            if VPS.objects.filter(uuid=new_uuid).exists():
                continue
            break
        serializer.save(uuid=new_uuid)
