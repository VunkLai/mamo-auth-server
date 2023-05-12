from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("application/", include("application.urls")),
    path("oauth/", include("oauth.urls")),
]
