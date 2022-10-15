from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

VPS_STATUSES = (
    ("START", "STARTED"),
    ("BLOCK", "BLOCKED"),
    ("STOP", "STOPPED"),
)


class VPS(models.Model):
    uuid = models.UUIDField(
        unique=True,
        help_text="VPS instance uuid",
        verbose_name="instance_uuid",
    )
    cpu = models.PositiveSmallIntegerField(
        help_text="Number of CPU cores",
        verbose_name="CPU_core_count",
        validators=(
            MinValueValidator(1, "Core count can not be less than one."),
        ),
    )
    ram = models.PositiveSmallIntegerField(
        help_text="VPS instance RAM size in GB",
        verbose_name="RAM_size_GB",
        validators=(
            MinValueValidator(1, "RAM size can not be less than one GB."),
            MaxValueValidator(128, "RAM size can not be more than 128 GB."),
        ),
    )
    hdd = models.PositiveSmallIntegerField(
        help_text="VPS instance HDD size in GB",
        verbose_name="HDD_size_GB",
        validators=(
            MinValueValidator(32, "HDD size can not be less than 32 GB."),
            MaxValueValidator(1024, "HDD size can not be more than 1024 GB."),
        ),
    )
    status = models.CharField(
        choices=VPS_STATUSES,
        max_length=64,
        help_text="VPS instance status",
        verbose_name="VPS_status",
    )

    class Meta:
        verbose_name = "VPS_instance"
        verbose_name_plural = "VPS_instances"
        ordering = ("-id",)

    def __str__(self):
        return f"{self.pk}:{self.cpu}:{self.ram}:{self.hdd}:{self.status}"
