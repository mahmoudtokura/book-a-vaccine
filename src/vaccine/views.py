from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.urls import reverse
from .models import Vaccine
from .forms import VaccineForm


# Create your views here.
class VaccineListView(View):
    def get(self, request):
        vaccines = Vaccine.objects.all()
        context = {"vaccines": vaccines}
        return render(request, "vaccine/vaccine-list.html", context)


class VaccineDetailView(View):
    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        context = {"vaccine": vaccine}
        return render(request, "vaccine/vaccine-detail.html", context)


class VaccineCreateView(View):
    form = VaccineForm
    template_name = "vaccine/create-vaccine.html"

    def get(self, request):
        context = {"form": self.form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse("vaccine:list"))
        return render(request, self.template_name, {"form": form})


class VaccineUpdateView(View):
    form = VaccineForm
    template_name = "vaccine/update-vaccine.html"

    def get(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        form = self.form(instance=vaccine)
        context = {"form": form}
        return render(request, self.template_name, context)

    def post(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        form = self.form(request.POST or None, instance=vaccine)
        if form.is_valid():
            form.save()
            messages.success(request, "Vaccine updated successfully")
            return redirect(reverse("vaccine:detail", args=[id]))
        return render(request, self.template_name, {"form": form})


class VaccineDeleteView(View):
    # We do not have a confirmation page, so we will use a modal on the detail page as confirmation
    def get(self, request, id):
        return redirect(reverse("vaccine:detail", args=[id]))

    def post(self, request, id):
        vaccine = get_object_or_404(Vaccine, id=id)
        vaccine.delete()
        return redirect(reverse("vaccine:list"))
