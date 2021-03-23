import json

from django.http import JsonResponse, HttpResponse
from server.settings import DATABASE


def get_config(request, operation):
    config = DATABASE
    if request.method == "GET":
        if operation == "data":
            url = f"postgresql+psycopg2://{config['USER']}:{config['PASSWORD']}@" \
                  f"{config['HOST']}:{config['PORT']}/{config['NAME']}"
            return JsonResponse(data={"url": url})
        elif operation == "auth":
            return JsonResponse(data={"config": config})
        return HttpRespone(status=404)
