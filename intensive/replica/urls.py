from django.urls import path
from replica.view import create_workers, check_replica, check_main_server, extra_check


urlpatterns = [
    path('create_workers/', create_workers, name='create_workers'),
    path('check_main_server/', check_main_server, name='check_main_server'),
    path('check_replica/', check_replica, name='check_replica'),
    path('extra_check/', extra_check, name='extra_check'),
]
