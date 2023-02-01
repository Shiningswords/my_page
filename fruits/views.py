from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def get_info_about_all_fruits(request, all_fruits):
    if all_fruits == 'apple':
        return HttpResponse('Яблоко')
    elif all_fruits == 'banana':
        return HttpResponse('Банан')
    else:
        return HttpResponseNotFound(f'Фрукт {all_fruits} не найден')