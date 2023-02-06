from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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
    redirected_url = reverse('week-name', args=(week_num,))
    return HttpResponseRedirect(redirected_url)


def get_info_about_all_week_str(request, all_week: str):
    return render(request, 'week_days/greeting.html')
