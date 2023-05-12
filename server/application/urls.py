from django.urls import path

from application import views

urlpatterns = [
    path("register", views.register),
]
