from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_info_about_all_week(request, all_week):
    if all_week == 'monday':
        return HttpResponse('Понедельник')
    elif all_week == 'tuesday':
        return HttpResponse('Вторник')
    elif all_week == 'wednesday':
        return HttpResponse('Среда')
    elif all_week == 'thursday':
        return HttpResponse('Четверг')
    elif all_week == 'friday':
        return HttpResponse('Пятница')
    elif all_week == 'saturday':
        return HttpResponse('Суббота')
    elif all_week == 'sunday':
        return HttpResponse('Воскресенье')
    else:
        return HttpResponseNotFound(f'Такого дня недели не существует ({all_week})')
