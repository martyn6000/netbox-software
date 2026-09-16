"""
Forms for NetBox Software Plugin.

For more information on NetBox forms, see:
https://docs.netbox.dev/en/stable/plugins/development/forms/
"""

from core.models import ObjectType
from dcim.models import Manufacturer
from django import forms
from django.contrib.contenttypes.models import ContentType
from netbox.forms import NetBoxModelForm
from utilities.forms import get_field_value
from utilities.forms.fields import ContentTypeChoiceField, DynamicModelChoiceField
from utilities.forms.widgets import HTMXSelect

from .models import LicenseAssignment, LicenseType, SoftwareLicense


class LicenseTypeForm(NetBoxModelForm):
    class Meta:
        model = LicenseType
        fields = ("name", "description", "color", "tags")


class SoftwareLicenseForm(NetBoxModelForm):
    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=True,
    )
    license_type = DynamicModelChoiceField(
        queryset=LicenseType.objects.all(),
        required=False,
        label="License Type",
    )

    class Meta:
        model = SoftwareLicense
        fields = (
            "manufacturer",
            "license_name",
            "friendly_name",
            "license_sku",
            "per_license_cost",
            "license_type",
            "tags",
        )


class LicenseAssignmentForm(NetBoxModelForm):
    software_license = DynamicModelChoiceField(
        queryset=SoftwareLicense.objects.all(),
        label="Software License",
    )
    object_type = ContentTypeChoiceField(
        queryset=ObjectType.objects.public(),
        label="Object Type",
        widget=HTMXSelect(),
    )
    object_id = forms.IntegerField(
        label="Object",
        required=False,
        disabled=True,
        help_text="Select an object type first.",
    )

    class Meta:
        model = LicenseAssignment
        fields = ("software_license", "object_type", "object_id", "tags")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        object_type_id = get_field_value(self, "object_type")
        model = None
        if object_type_id:
            try:
                model = ContentType.objects.get(pk=object_type_id).model_class()
            except (ContentType.DoesNotExist, ValueError):
                model = None

        if model is not None:
            self.fields["object_id"] = DynamicModelChoiceField(
                queryset=model.objects.all(),
                label="Object",
                selector=True,
            )
            if self.instance.pk and self.instance.object_type_id == int(object_type_id):
                self.fields["object_id"].initial = self.instance.assigned_object

    def clean(self):
        super().clean()

        # The object_id field yields a model instance; store its primary key on the instance instead.
        selected_object = self.cleaned_data.get("object_id")
        if selected_object is not None:
            self.cleaned_data["object_id"] = selected_object.pk

        return self.cleaned_data
