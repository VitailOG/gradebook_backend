from rest_framework import status
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


class Process500:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception) -> HttpResponse:
        if request.path.startswith('/admin/'):
            return render(request, '../templates/error.html', {"error": str(exception)})

        return JsonResponse(
            {
                "error": True,
                "message": str(exception)
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
