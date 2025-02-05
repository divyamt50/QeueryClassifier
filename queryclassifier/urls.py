from django.contrib import admin
from django.urls import path, include
from classifier.views import home

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/", include("classifier.urls")),  # Include classifier API
]
