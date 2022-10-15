from django.contrib import admin

from .models import VPS


class VPSAdmin(admin.ModelAdmin):
    list_display = ("id", "uuid", "cpu", "ram", "hdd", "status",)
    empty_value_display = "-empty-"


admin.site.register(VPS, VPSAdmin)
