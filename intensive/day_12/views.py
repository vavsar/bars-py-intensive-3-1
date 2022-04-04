from django.views.decorators.csrf import csrf_exempt

from day_12.controller import main_controller


@csrf_exempt
def main_view(request):
    """
    Роутинг запросов для перенаправления к пакам,
    зарегистрированным в контроллере
    """
    return main_controller.process_request(request)
