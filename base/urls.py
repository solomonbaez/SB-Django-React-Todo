from django.urls import path
from . import views

urlpatterns = [
    path("health-check/", views.healthCheck, name="health-check"),
    path("", views.homeView, name="home"),
    path("user-login/", views.loginView, name="user-login"),
    path("user-logout/", views.logoutView, name="user-logout"),
    path("create-note/", views.createNote, name="create-note"),
    path("update-note/<str:pk>", views.updateNote, name="update-note"),
]
