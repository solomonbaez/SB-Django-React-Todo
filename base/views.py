from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, User
from .forms import noteForm


@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "home": "",
        "create-note": "/create-note/",
        "update-note": "/update-note/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def healthCheck(request):
    return render(request, "base/health-check.html")


@api_view(["GET", "POST"])
def homeView(request):
    try:
        notes = Note.objects.filter(user=request.user)
    except:
        messages.add_message(request, messages.INFO, "Please log in!")
        notes = []

    context = {"notes": notes}

    if request.method == "POST":
        note = Note.objects.get(id=request.POST.get("id"))
        title = note.title
        note.delete()

        messages.add_message(
            request, messages.INFO, (title + " " + "has been deleted.")
        )
        return redirect("home")

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
    logout(request)

    return redirect("home")


def createNote(request):
    form = noteForm()

    if request.method == "POST":
        Note.objects.create(
            user=request.user,
            title=request.POST.get("title"),
            description=request.POST.get("description"),
        )

        return redirect("home")

    context = {"form": form, "new_or_update": "new"}
    return render(request, "base/create-note.html", context)


def updateNote(request, pk):
    note = Note.objects.get(id=pk)
    form = noteForm(instance=note)

    if request.method == "POST":
        note.title = request.POST.get("title")
        note.description = request.POST.get("description")
        note.save()

        messages.add_message(
            request, messages.INFO, (note.title + " " + "has been updated.")
        )
        return redirect("home")

    context = {"form": form, "note": note, "new_or_update": "new"}
    return render(request, "base/create-note.html", context)
