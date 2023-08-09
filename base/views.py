from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, User
from .forms import noteForm
from .serializers import noteSerializer


##############################API##############################
@api_view(["GET"])
def apiOverview(request):
    api_urls = {
        "health-check": "/health-check/",
        "notes": "/notes/",
        "create-note": "/create-note/",
        "update-note": "/update-note/<str:pk>",
    }

    return Response(api_urls)


@api_view(["GET"])
def healthCheck(request):
    return Response(HttpResponse.status_code)


@api_view(["GET"])
def notesView(request):
    notes = Note.objects.all()
    serialized_notes = noteSerializer(notes, many=True)

    return Response(serialized_notes.data)


@api_view(["GET"])
def notesDetailView(request, pk):
    note = Note.objects.get(id=pk)
    serialized_note = noteSerializer(note, many=False)

    return Response(serialized_note.data)


@api_view(["POST"])
def apiCreateNote(request):
    serializer = noteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def apiUpdateNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = noteSerializer(instance=note, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def apiDeleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response("Item deleted!")


##############################API##############################


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
