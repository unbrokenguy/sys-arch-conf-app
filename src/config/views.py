from abc import ABC

from django.http import JsonResponse, HttpResponse
from server.settings import DATABASE


class ConfigStrategy(ABC):
    def __init__(self):
        self._config = None

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config) -> None:
        self._config = config


class AuthConfigStrategy(ConfigStrategy):
    @property
    def config(self):
        return {"config": self._config}

    @config.setter
    def config(self, config) -> None:
        self._config = config


class DataConfigStrategy(ConfigStrategy):
    @property
    def config(self):
        return {
            "url": f"postgresql+psycopg2://{self._config['USER']}:{self._config['PASSWORD']}@"
            f"{self._config['HOST']}:{self._config['PORT']}/{self._config['NAME']}"
        }

    @config.setter
    def config(self, config) -> None:
        self._config = config


def choose_strategy(operation):
    if operation == "data":
        strategy = DataConfigStrategy()
    elif operation == "auth":
        strategy = AuthConfigStrategy()
    else:
        raise NotImplementedError
    strategy.config = DATABASE
    return strategy


def get_config(request, operation):
    strategy = choose_strategy(operation)
    if request.method == "GET":
        try:
            return JsonResponse(data=strategy.config)
        except NotImplementedError:
            return HttpResponse(status=501)
    return HttpResponse(status=400)
