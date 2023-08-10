from django.shortcuts import render, redirect
from rest_framework.views import APIView
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


class GetNotes(APIView):
    def get(self, request):
        notes = Note.objects.all().order_by("-updated")
        serializer = noteSerializer(notes, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        note = Note.objects.create(
            title=data["title"],
            description=data["description"],
        )
        serializer = noteSerializer(note, many=False)

        return Response(serializer.data)


class GetNote(APIView):
    def get(self, request, pk):
        note = Note.objects.get(id=pk)
        serializer = noteSerializer(note, many=False)

        return Response(serializer.data)

    def put(self, request, pk):
        note = Note.objects.get(id=pk)
        serializer = noteSerializer(instance=note, data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    def delete(self, request, pk):
        note = Note.objects.get(id=pk)
        note.delete()

        return Response("Note Deleted!")


#############################API##############################
