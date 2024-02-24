from django import forms

from .models import Vaccine


class VaccineForm(forms.ModelForm):
    name = forms.CharField(
        label="Vaccine Name", widget=forms.TextInput(attrs={"class": "form-control"})
    )
    description = forms.CharField(
        label="Vaccine Description",
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )
    number_of_doses = forms.IntegerField(
        label="Number of Doses",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    interval = forms.IntegerField(
        label="Interval between Doses",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    storage_temperature = forms.IntegerField(
        label="Storage Temperature",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )
    minimum_age = forms.IntegerField(
        label="Minimum Age",
        widget=forms.NumberInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Vaccine
        fields = "__all__"
