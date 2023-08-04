from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Note, User
from .forms import noteForm


def healthCheck(request):
    return render(request, "base/health-check.html")


def homeView(request):
    notes = Note.objects.filter(user=request.user)
    context = {"notes": notes}
    return render(request, "base/home.html", context)


def loginView(request):
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        user = User.objects.get(username=username)
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")

        else:
            print("Failed to authenticate")

    return render(request, "base/user-login.html")


def logoutView(request):
    return render(request, "base/home.html")


def createNote(request):
    form = noteForm()

    if request.method == "POST":
        Note.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            description=request.POST.get("description"),
        )

        return redirect("home")

    return render(request, "base/create-note.html", {"form": form})
