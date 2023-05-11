from django.http import HttpRequest, JsonResponse

from rest_framework.decorators import api_view


@api_view(["post"])
def register(request: HttpRequest) -> JsonResponse:
    return JsonResponse({})


@api_view(["post"])
def sign_in(request: HttpRequest):
    pass


@api_view(["post"])
def logout(request: HttpRequest):
    pass
