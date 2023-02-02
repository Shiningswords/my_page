from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

week = {
    1: 'Понедельник',
    2: 'Вторник',
    3: 'Среда',
    4: 'Четверг',
    5: 'Пятница',
    6: 'Суббота',
    7: 'Воскресенье'
}


def get_info_about_all_week(request, all_week: int):
    description = week.get(all_week, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Такого дня недели не существует ({all_week})')
