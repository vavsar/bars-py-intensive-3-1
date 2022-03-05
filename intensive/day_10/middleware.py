import json

from django.http import HttpResponse
from django.http import JsonResponse

from django.utils.deprecation import (
    MiddlewareMixin,
)

from timeit import default_timer as timer

import sys


class StatisticMiddleware:
    """
    Компонент вычисляющий время выполнения запроса на сервере и размер ответа в байтах.
    Отображает значения в консоли приложения
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        time_before = timer()

        response = self.get_response(request)

        execution_time = timer() - time_before
        print('Время выполнения запроса: ', execution_time)
        print('Размер ответа в байтах: ', sys.getsizeof(response))

        return response


class FormatterMiddleware:
    """
    Компонент форматирующий Json ответ в HttpResponse
    {'key': value} => <p>key = value</p>
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if isinstance(response, JsonResponse):
            content = json.loads(response.content)
            output = []
            for key, value in content.items():
                output.append(f'<p>{key} = {value}</p>')
            response = HttpResponse(output)

        return response


class CheckErrorMiddleware(MiddlewareMixin):
    """
        Перехватывает необработанное исключение в представлении и отображает ошибку в виде
        "Ошибка: {exception}"
    """
    @staticmethod
    def process_exception(request, exception):
        return HttpResponse(f'Ошибка: {exception}')
