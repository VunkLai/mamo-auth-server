from http import HTTPStatus

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from application.models import Application


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return render(request, "application/register.html")

    if request.method == "POST":
        name = request.POST["name"]
        redirect_urls = request.POST["redirect_urls"]
        application = Application.objects.register(name, redirect_urls)
        context = {
            "name": application.name,
            "redirect_urls": application.redirect_urls,
            "client_id": application.client_id,
            "client_secret": application.client_secret,
        }
        return render(request, "application/information.html", context)

    return HttpResponse("", status=HTTPStatus.METHOD_NOT_ALLOWED)
