from django.shortcuts import render


def healthCheck(request):
    return render(request, "base/health-check.html")
