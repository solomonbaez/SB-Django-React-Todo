from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.apiOverview, name="api"),
    path("health-check/", views.healthCheck, name="health-check"),
    path("notes", views.notesView, name="notes"),
    path("notes/<str:pk>", views.notesDetailView, name="notes-details"),
    path("api-create-note", views.apiCreateNote, name="api-create-note"),
    path("api-update-note/<str:pk>", views.apiUpdateNote, name="api-update-note"),
    path("api-delete-note/<str:pk>", views.apiDeleteNote, name="api-delete-note"),
    path("", views.homeView, name="home"),
    path("user-login/", views.loginView, name="user-login"),
    path("user-logout/", views.logoutView, name="user-logout"),
    path("create-note/", views.createNote, name="create-note"),
    path("update-note/<str:pk>", views.updateNote, name="update-note"),
]
