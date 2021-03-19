import json

from django.http import JsonResponse, HttpResponse


def get_config(request, operation):
    if request.method == "GET":
        config = json.loads(open("config.json", 'r').read())
        if operation == "data":
            config = config[0]
            url = f"postgresql+psycopg2://{config['USER']}:{config['PASSWORD']}@" \
                  f"{config['HOST']}:{config['PORT']}/{config['NAME']}"
            return JsonResponse(data={"url": url})
        elif operation == "auth":
            return JsonResponse(data={"config": config})
        return HttpRespone(status=404)
