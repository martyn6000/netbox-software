"""
Models for NetBox Software Plugin.

For more information on NetBox models, see:
https://docs.netbox.dev/en/stable/plugins/development/models/

For NetBox model features (tags, custom fields, change logging, etc.), see:
https://docs.netbox.dev/en/stable/development/models/#netbox-model-features
"""

from dcim.models import Manufacturer
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from netbox.choices import ColorChoices
from netbox.models import NetBoxModel
from utilities.fields import ColorField


class LicenseType(NetBoxModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200, blank=True)
    color = ColorField(default=ColorChoices.COLOR_GREY)

    class Meta:
        app_label = "netbox_software"
        ordering = ("name",)
        verbose_name = "License Type"
        verbose_name_plural = "License Types"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("plugins:netbox_software:licensetype", args=[self.pk])


class SoftwareLicense(NetBoxModel):
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.PROTECT,
        related_name="software_licenses",
    )
    license_name = models.CharField(max_length=150)
    friendly_name = models.CharField(max_length=150, blank=True)
    license_sku = models.CharField(max_length=100)
    per_license_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True,
        help_text="Unit cost per license",
    )
    license_type = models.ForeignKey(
        to=LicenseType,
        on_delete=models.PROTECT,
        related_name="software_licenses",
        blank=True,
        null=True,
    )

    class Meta:
        app_label = "netbox_software"
        ordering = ("license_name",)
        verbose_name = "Software License"
        verbose_name_plural = "Software Licenses"

    def __str__(self):
        return self.license_name

    def get_absolute_url(self):
        return reverse("plugins:netbox_software:softwarelicense", args=[self.pk])

    @property
    def assignment_count(self):
        return self.assignments.count()


class LicenseAssignment(NetBoxModel):
    software_license = models.ForeignKey(
        to=SoftwareLicense,
        on_delete=models.PROTECT,
        related_name="assignments",
    )
    object_type = models.ForeignKey(
        to=ContentType,
        on_delete=models.PROTECT,
        related_name="+",
    )
    object_id = models.PositiveBigIntegerField()
    assigned_object = GenericForeignKey(
        ct_field="object_type",
        fk_field="object_id",
    )

    class Meta:
        app_label = "netbox_software"
        ordering = ("software_license",)
        verbose_name = "License Assignment"
        verbose_name_plural = "License Assignments"
        indexes = (models.Index(fields=("object_type", "object_id")),)
        constraints = (
            models.UniqueConstraint(
                fields=("software_license", "object_type", "object_id"),
                name="%(app_label)s_%(class)s_unique_license_object",
            ),
        )

    def __str__(self):
        if self.assigned_object:
            return f"{self.software_license} -> {self.assigned_object}"
        return str(self.software_license)

    def get_absolute_url(self):
        return reverse("plugins:netbox_software:licenseassignment", args=[self.pk])
