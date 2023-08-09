from django.urls import path
from . import views

urlpatterns = [
    path("api", views.apiOverview, name="api"),
    path("health-check", views.healthCheck, name="health-check"),
    path("notes", views.notesView, name="notes"),
    path("notes/<str:pk>", views.notesDetailView, name="notes-details"),
    path("notes/create/", views.apiCreateNote, name="create-note"),
    path("notes/<str:pk>/update", views.apiUpdateNote, name="update-note"),
    path("notes/<str:pk>/delete", views.apiDeleteNote, name="delete-note"),
    # path("", views.homeView, name="home"),
    # path("user-login", views.loginView, name="user-login"),
    # path("user-logout", views.logoutView, name="user-logout"),
    # path("create-note/", views.createNote, name="create-note"),
    # path("update-note/<str:pk>", views.updateNote, name="update-note"),
]
