from django.urls import path
from .views import classify_query

urlpatterns = [
    path("classify/", classify_query, name="classify_query"),
]
