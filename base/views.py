from django.shortcuts import render


def healthCheck(request):
    return render(request, "base/health-check.html")


def homeView(request):
    return render(request, "base/home.html")


def loginView(request):
    return render(request, "base/home.html")


def logoutView(request):
    return render(request, "base/home.html")