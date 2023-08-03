from django.shortcuts import render
from .models import Note


def healthCheck(request):
    return render(request, "base/health-check.html")


def homeView(request):
    notes = Note.objects.all()
    context = {"notes": notes}
    return render(request, "base/home.html", context)


def loginView(request):
    return render(request, "base/home.html")


def logoutView(request):
    return render(request, "base/home.html")
