from django.urls import path
from .views import classify_query,home

urlpatterns = [
    path("", home),
    path("classify/", classify_query, name="classify_query"),
]
