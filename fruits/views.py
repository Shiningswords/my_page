from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

fruits = {
    'apple': 'Яблоко',
    'banana': 'Банан',
    'ananas': 'Ананас',
    'lemon': 'Лимон',
    'mango': 'Манго'
}


def get_info_about_all_fruits(request, all_fruits: str):
    description = fruits.get(all_fruits, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Фрукт {all_fruits} не найден')


def get_info_about_all_fruits_by_num(request, all_fruits: int):
    fruits_list = list(fruits)
    if all_fruits > len(fruits_list) or all_fruits < 1:
        return HttpResponseNotFound(f'Такой номер фрукта отсутствует ({all_fruits})')
    fruit_num = fruits_list[all_fruits - 1]
    redirect_url = reverse('fruits-name', args=(fruit_num,))
    return HttpResponseRedirect(redirect_url)
