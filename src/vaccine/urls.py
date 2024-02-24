from django.urls import path

from .views import (
    VaccineDetailView,
    VaccineListView,
    VaccineCreateView,
    VaccineUpdateView,
    VaccineDeleteView,
)

app_name = "vaccine"

urlpatterns = [
    path("", VaccineListView.as_view(), name="list"),
    path("create/", VaccineCreateView.as_view(), name="create"),
    path("<int:id>/", VaccineDetailView.as_view(), name="detail"),
    path("<int:id>/update/", VaccineUpdateView.as_view(), name="update"),
    path("<int:id>/delete/", VaccineDeleteView.as_view(), name="delete"),
]
