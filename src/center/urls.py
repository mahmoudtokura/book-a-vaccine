from django.urls import path
from . import views

app_name = "center"

urlpatterns = [
    path("", views.center_list, name="list"),
    path("<int:id>/", views.center_detail, name="detail"),
    path("create/", views.center_create, name="create"),
    path("<int:id>/update/", views.center_update, name="update"),
    path("<int:id>/delete/", views.center_delete, name="delete"),
]
