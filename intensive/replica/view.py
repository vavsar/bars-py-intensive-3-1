from django.http import HttpResponse

from replica.models import Worker


def create_workers(request):
    counter = 1
    Worker.objects.create(name=f'worker{counter}')
    counter += 1
    Worker.objects.create(name=f'worker{counter}')
    counter += 1
    Worker.objects.create(name=f'worker{counter}')
    counter += 1

    return HttpResponse('3 workers created')


def check_main_server(request):
    response = Worker.objects.all().using('default')

    return HttpResponse(response)


def check_replica(request):
    response = Worker.objects.all().using('replica')

    return HttpResponse(response)


def extra_check(request):
    try:
        response = Worker.objects.all().using('default')
    except:
        response = Worker.objects.all().using('replica')

    return HttpResponse(response)
