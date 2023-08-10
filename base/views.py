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


@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "GET":
        notes = Note.objects.all().order_by("-updated")
        serializer = noteSerializer(notes, many=True)

    elif request.method == "POST":
        data = request.data
        note = Note.objects.create(
            title=data["title"],
            description=data["description"],
        )
        serializer = noteSerializer(note, many=False)

    return Response(serializer.data)


@api_view(["GET", "PUT", "DELETE"])
def getNote(request, pk):
    note = Note.objects.get(id=pk)

    if request.method == "GET":
        serializer = noteSerializer(note, many=False)

    elif request.method == "PUT":
        serializer = noteSerializer(instance=note, data=request.data)

    elif request.method == "DELETE":
        note.delete()
        return Response("Note Deleted!")

    return Response(serializer.data)


#############################API##############################
