from django.http import (
    JsonResponse,
)

from django.views import (
    View,
)

from day_19.models import Worker


class Task1View(View):
    """
    Добавляет две новые записи в таблицу worker при открытии страницы
    """

    def get(self, request, **kwargs):
        Worker.objects.bulk_create([
            Worker(fio='Петров Петр Петрович'),
            Worker(fio='Иванов Иван Иванович')
        ])

        return JsonResponse(
            data=dict(result='Были добавлены 2 записи в таблицу worker'),
            json_dumps_params=dict(ensure_ascii=False, default=str),
        )


class Task2View(View):
    """
    Выводит записи из таблицы worker из основной базы
    """

    def get(self, request, **kwargs):
        result = Worker.objects.using('main').all().values()
        result = list(result)

        return JsonResponse(
            data=dict(result_from_main=result),
            json_dumps_params=dict(ensure_ascii=False, default=str),
        )


class Task3View(View):
    """
    Выводит записи из таблицы worker из базы-репликации основной базы
    """

    def get(self, request, **kwargs):
        result = Worker.objects.using('replica').all().values()
        result = list(result)

        return JsonResponse(
            data=dict(result_from_replica=result),
            json_dumps_params=dict(ensure_ascii=False, default=str),
        )


class Task4View(View):
    """
    Выводит записи из таблицы worker из основной базы если она доступна,
    иначе выводит записи из базы-реплики
    """

    def get(self, request, **kwargs):
        result = Worker.objects.using('main').all().values()
        try:
            result = list(result)
        except:
            result = Worker.objects.using('replica').all().values()
            result = list(result)

        return JsonResponse(
            data=dict(result=result),
            json_dumps_params=dict(ensure_ascii=False, default=str),
        )