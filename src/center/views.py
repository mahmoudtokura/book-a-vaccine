from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Center
from .forms import CenterForm

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
