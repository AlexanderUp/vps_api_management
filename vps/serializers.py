from rest_framework import serializers

from .models import VPS


class VPSSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = VPS
        fields = ("id", "uuid", "cpu", "ram", "hdd", "status",)
