from django.urls import path

from oauth import views

urlpatterns = [
    path("register/", views.register),
    path("sign-in/", views.sign_in),
    path("logout/", views.logout),
]
