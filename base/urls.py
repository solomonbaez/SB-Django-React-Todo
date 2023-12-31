from django.urls import path
from . import views

urlpatterns = [
    path("api", views.apiOverview, name="api"),
    path("health-check", views.healthCheck, name="health-check"),
    path("notes", views.GetNotes.as_view(), name="notes"),
    path("notes/<str:pk>", views.GetNote.as_view(), name="notes-details"),
]
