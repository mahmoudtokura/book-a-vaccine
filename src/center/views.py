from typing import Any
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import generic
from .models import Center, Storage
from .forms import CenterForm, StorageForm

# Create your views here.


def center_list(request):
    object_list = Center.objects.all()
    context = {
        "centers": object_list,
    }
    return render(request, "center/center-list.html", context)


def center_detail(request, id):
    center = get_object_or_404(Center, id=id)
    context = {
        "center": center,
    }
    return render(request, "center/center-detail.html", context)


def center_create(request):
    form = CenterForm()
    if request.method == "POST":
        form = CenterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Center created successfully")
            return redirect(reverse("center:list"))
        return render(request, "center/create-center.html", {"form": form})
    else:
        context = {
            "form": form,
        }
    return render(request, "center/create-center.html", context)


def center_update(request, id):
    center = get_object_or_404(Center, id=id)
    form = CenterForm(instance=center)
    if request.method == "POST":
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            messages.success(request, "Center updated successfully")
            return redirect(reverse("center:detail", args=[center.id]))
        return render(request, "center/update-center.html", {"form": form})
    else:
        context = {
            "form": form,
        }
    return render(request, "center/update-center.html", context)


def center_delete(request, id):
    center = get_object_or_404(Center, id=id)
    center.delete()
    messages.success(request, "Center deleted successfully")
    return redirect(reverse("center:list"))


class StorageListView(generic.ListView):
    model = Storage
    template_name = "storage/storage-list.html"
    context_object_name = "object_list"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["center_id"] = self.kwargs.get("center_id")
        return context

    def get_queryset(self):
        center_id = self.kwargs.get("center_id")
        return Storage.objects.filter(center__id=center_id)


class StorageDetailView(generic.DetailView):
    model = Storage
    template_name = "storage/storage-detail.html"
    context_object_name = "object"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["available_quantity"] = (
            self.object.total_quantity - self.object.booked_quantity
        )
        context["center_id"] = self.kwargs.get("center_id")
        return context


class StorageCreateView(generic.CreateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage-create.html"

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["center_id"] = self.kwargs.get("center_id")
        return kwargs

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial["center"] = Center.objects.get(id=self.kwargs.get("center_id"))
        return initial

    def form_valid(self, form):
        center_id = self.kwargs.get("center_id")
        center = get_object_or_404(Center, id=center_id)
        form.instance.center = center
        return super().form_valid(form)

    def get_success_url(self):
        center_id = self.kwargs.get("center_id")
        return reverse("center:storage", args=[center_id])


class StorageUpdateView(generic.UpdateView):
    model = Storage
    form_class = StorageForm
    template_name = "storage/storage-update.html"

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs["center_id"] = self.kwargs.get("center_id")
        return kwargs

    def get_success_url(self):
        center_id = self.kwargs.get("center_id")
        storage_pk = self.kwargs.get("pk")
        return reverse("center:storage-detail", args=[center_id, storage_pk])


class StorageDeleteView(generic.DeleteView):
    model = Storage
    template_name = "storage/storage-delete.html"

    def get_success_url(self):
        center_id = self.kwargs.get("center_id")
        return reverse("center:storage", args=[center_id])