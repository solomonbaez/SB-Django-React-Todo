from django.urls import path
from . import views

urlpatterns = [
    path("api", views.apiOverview, name="api"),
    path("health-check", views.healthCheck, name="health-check"),
    path("notes", views.notesView, name="notes"),
    path("notes/<str:pk>", views.notesDetailView, name="notes-details"),
    path("create/", views.apiCreateNote, name="create-note"),
    path("notes/<str:pk>/update", views.apiUpdateNote, name="update-note"),
    path("notes/<str:pk>/delete", views.apiDeleteNote, name="delete-note"),
]
