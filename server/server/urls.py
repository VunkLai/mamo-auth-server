from django.urls import include, path

urlpatterns = [
    path("oauth/", include("oauth.urls")),
]
