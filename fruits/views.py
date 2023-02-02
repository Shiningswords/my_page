from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

fruits = {
    'apple': 'Яблоко',
    'banana': 'Банан',
    'ananas': 'Ананас',
    'lemon': 'Лимон',
    'mango': 'Манго'
}


def get_info_about_all_fruits(request, all_fruits):
    description = fruits.get(all_fruits, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Фрукт {all_fruits} не найден')
