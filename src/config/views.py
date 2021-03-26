from abc import ABC

from django.http import JsonResponse, HttpResponse
from server.settings import DATABASE


class ConfigStrategy(ABC): # Чтобы обращаться к вычисляемым полям как к атрибутам
    def __init__(self): # Конструктор
        self._config = None

    @property # Оборачиваем в property()
    def config(self):
        return self._config

    @config.setter # сеттер
    def config(self, config) -> None:
        self._config = config


class AuthConfigStrategy(ConfigStrategy): # Если был выбран метод auth
    @property
    def config(self):
        return {"config": self._config} # Возвращаем конфиг

    @config.setter # Сеттер
    def config(self, config) -> None:
        self._config = config


class DataConfigStrategy(ConfigStrategy): # Если был выбран метод data
    @property
    def config(self): # Возвращаем строку подключения
        return {
            "url": f"postgresql+psycopg2://{self._config['USER']}:{self._config['PASSWORD']}@"
            f"{self._config['HOST']}:{self._config['PORT']}/{self._config['NAME']}"
        }

    @config.setter # Сеттер
    def config(self, config) -> None:
        self._config = config


def choose_strategy(operation): # Опираясь на выбор пользователя вызываем нужную нам стратегию
    if operation == "data":
        strategy = DataConfigStrategy()
    elif operation == "auth":
        strategy = AuthConfigStrategy()
    else:
        raise NotImplementedError # Перехватываем ошибку о том, что метод не может быть реализован
    strategy.config = DATABASE # Присваиваем конфиги
    return strategy


def get_config(request, operation): # Получение конфига
    strategy = choose_strategy(operation) # Определяем что выбрал пользователь
    if request.method == "GET": # Если метод запроса GET
        try:
            return JsonResponse(data=strategy.config) # Возвращаем конфиг в формате JSON нужной стратегии
        except NotImplementedError: # Перехватываем ошибку, если метод не может быть реализован
            return HttpResponse(status=404) # Возвращаем 404 - сервер не смог найти запрос
    return HttpResponse(status=405) # Если условие не выполняется, то ошибка - не существует реализации метода
