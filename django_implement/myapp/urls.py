from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("webchat", views.webchat, name="webchat"),
]
