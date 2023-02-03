from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

fruits = {
    'apple': 'Яблоко',
    'banana': 'Банан',
    'ananas': 'Ананас',
    'lemon': 'Лимон',
    'mango': 'Манго',
    'strawberry': 'Клубника',
    'cherry': 'Вишня',
    'raspberry': 'Малина'
}

fruits_type = {
    'fruits': ['apple', 'banana', 'ananas', 'lemon', 'mango'],
    'berry': ['strawberry', 'cherry', 'raspberry']
}


def index(request):
    li_elements = ''
    for fruit in fruits:
        redirect_path = reverse('fruits-name', args=(fruit,))
        li_elements += '<li>' + f'<a href={redirect_path}>' + fruit.title() + '</a>' + '</li>'
    ol_elements = '<ol>' + li_elements + '</ol>'
    return HttpResponse(ol_elements)


def types(request):
    li_elements = ''
    for t in fruits_type:
        redirect_path = reverse('type_f', args=(t,))
        li_elements += '<li>' + f'<a href={redirect_path}>' + t.title() + '</a>' + '</li>'
    ol_elements = '<ol>' + li_elements + '</ol>'
    return HttpResponse(ol_elements)


def types_f(request, type_fruits):
    li_elements = ''
    for t in fruits_type[type_fruits]:
        redirect_path = reverse('fruits-name', args=(t,))
        li_elements += '<li>' + f'<a href={redirect_path}>' + t.title() + '</a>' + '</li>'
    ol_elements = '<ol>' + li_elements + '</ol>'
    return HttpResponse(ol_elements)


def get_info_about_all_fruits(request, all_fruits: str):
    description = fruits.get(all_fruits, None)
    if description:
        return HttpResponse(f'<h2>{description}</h2>')
    else:
        return HttpResponseNotFound(f'Фрукт {all_fruits} не найден')


def get_info_about_all_fruits_by_num(request, all_fruits: int):
    fruits_list = list(fruits)
    if all_fruits > len(fruits_list) or all_fruits < 1:
        return HttpResponseNotFound(f'Такой номер фрукта отсутствует ({all_fruits})')
    fruit_num = fruits_list[all_fruits - 1]
    redirect_url = reverse('fruits-name', args=(fruit_num,))
    return HttpResponseRedirect(redirect_url)
