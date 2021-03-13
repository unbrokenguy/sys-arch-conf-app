import json

from django.http import JsonResponse
from django.shortcuts import render


def get_config(request):
    if request.method == "GET":
        config = json.loads(open("config.json", 'r').read())
        config = config[0]
        url = f"postgresql+psycopg2://{config['USER']}:{config['PASSWORD']}@" \
              f"{config['HOST']}:{config['PORT']}/{config['NAME']}"
        return JsonResponse(data={"url": url})
