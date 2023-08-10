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
    notes = Note.objects.all().order_by("-updated")
    serialized_notes = noteSerializer(notes, many=True)

    return Response(serialized_notes.data)


@api_view(["GET"])
def notesDetailView(request, pk):
    note = Note.objects.get(id=pk)
    serialized_note = noteSerializer(note, many=False)

    return Response(serialized_note.data)


@api_view(["POST"])
def apiCreateNote(request):
    data = request.data
    note = Note.objects.create(
        title=data["title"],
        description=data["description"],
    )
    serializer = noteSerializer(note, many=False)

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

    return Response("Note deleted!")


##############################API##############################
