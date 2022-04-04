from django.conf.urls import url
from day_12.views import main_view

# Переадресация всех запросов приложения в main_view
urlpatterns = (
    url('', main_view),
)
