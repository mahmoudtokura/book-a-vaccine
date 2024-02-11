from django.shortcuts import render


def index(request):
    context = {"message": "Django"}
    return render(request, "site/index.html", context)
