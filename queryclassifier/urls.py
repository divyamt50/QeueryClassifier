# queryclassifier/urls.py
from django.contrib import admin
from django.urls import path, include
from classifier.views import home

urlpatterns = [
    path("", home, name="home"),  # This is for the home page
    path("admin/", admin.site.urls),
    path("api/", include("classifier.urls")),  # Include classifier URLs for the API
]
