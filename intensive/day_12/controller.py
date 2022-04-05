from m3.actions import ActionController


class MainController(ActionController):
    """
    Переопределим в контроллере обработку запроса
    """
    def process_request(self, request):
        # удалим конечный слэш
        if request.path.endswith('/'):
            request.path = request.path[:-1]

        return super().process_request(request)


# Создадим экземпляр контроллера
main_controller = MainController('/demo')
