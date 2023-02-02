from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

week = {
    'monday': 'Понедельник',
    'tuesday': 'Вторник',
    'wednesday': 'Среда',
    'thursday': 'Четверг',
    'friday': 'Пятница',
    'saturday': 'Суббота',
    'sunday': 'Воскресенье'
}


def get_info_about_all_week(request, all_week: int):
    week_list = list(week)
    if all_week > len(week_list) or all_week < 1:
        return HttpResponseNotFound(f'Такого дня недели не существует ({all_week})')
    week_num = week_list[all_week - 1]
    return HttpResponseRedirect(f'/week_days/{week_num}')


def get_info_about_all_week_str(request, all_week: str):
    description = week.get(all_week, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Такого дня недели не существует ({all_week})')
