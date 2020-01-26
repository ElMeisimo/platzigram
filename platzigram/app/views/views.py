from django.http import HttpResponse, JsonResponse
from datetime import datetime

def time(request):
    return HttpResponse('The time is {now}'.format(now=datetime.now().strftime('%H:%m')))

def hello(request):
    return HttpResponse('hello world!')

def sort(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',') ]
    numbers.sort()

    return JsonResponse(numbers, safe=False)