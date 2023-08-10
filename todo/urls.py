from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    # api/ to prevent conflicts with React
    path("api/", include("base.urls")),
    # point the template to frontend
    path("", TemplateView.as_view(template_name="index.html")),
]
