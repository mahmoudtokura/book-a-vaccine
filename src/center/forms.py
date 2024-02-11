from django import forms

from .models import Center


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
