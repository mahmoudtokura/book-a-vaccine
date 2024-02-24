from django import forms

from .models import Center, Storage


class CenterForm(forms.ModelForm):
    """Form definition for Center."""

    name = forms.CharField(
        label="Center Name",
        max_length=50,
        required=True,
        help_text="Enter the name of the center",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    address = forms.CharField(
        label="Center Address",
        max_length=100,
        required=True,
        help_text="Enter the address of the center",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    class Meta:
        """Meta definition for Centerform."""

        model = Center
        fields = "__all__"


class StorageForm(forms.ModelForm):
    """Form definition for Storage."""

    def __init__(self, center_id, *args, **kwargs):
        super(StorageForm, self).__init__(*args, **kwargs)
        self.fields["center"].initial = center_id
        self.fields["center"].disabled = True
        self.fields["booked_quantity"].disabled = True
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

    class Meta:
        """Meta definition for Storageform."""

        model = Storage
        fields = "__all__"
