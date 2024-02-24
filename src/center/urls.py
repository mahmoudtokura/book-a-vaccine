from django.urls import path
from . import views

app_name = "center"

urlpatterns = [
    path("", views.center_list, name="list"),
    path("<int:id>/", views.center_detail, name="detail"),
    path("create/", views.center_create, name="create"),
    path("<int:id>/update/", views.center_update, name="update"),
    path("<int:id>/delete/", views.center_delete, name="delete"),
    # storage urls
    path("<int:center_id>/storage/", views.StorageListView.as_view(), name="storage"),
    path(
        "<int:center_id>/storage/<int:pk>",
        views.StorageDetailView.as_view(),
        name="storage-detail",
    ),
    path(
        "<int:center_id>/storage/create/",
        views.StorageCreateView.as_view(),
        name="storage-create",
    ),
    path(
        "<int:center_id>/storage/<int:pk>/update/",
        views.StorageUpdateView.as_view(),
        name="storage-update",
    ),
    path(
        "<int:center_id>/storage/<int:pk>/delete/",
        views.StorageDeleteView.as_view(),
        name="storage-delete",
    ),
]
