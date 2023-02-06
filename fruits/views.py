from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    fruits_list = list(fruits)
    data = {
        'fruits_list': fruits_list
    }
    return render(request, 'fruits/index.html', data)


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
    description = fruits.get(all_fruits)
    data = {
        'description_fruits': description
    }
    return render(request, 'fruits/info_fruits.html', data)


def get_info_about_all_fruits_by_num(request, all_fruits: int):
    fruits_list = list(fruits)
    if all_fruits > len(fruits_list) or all_fruits < 1:
        return HttpResponseNotFound(f'Такой номер фрукта отсутствует ({all_fruits})')
    fruit_num = fruits_list[all_fruits - 1]
    redirect_url = reverse('fruits-name', args=(fruit_num,))
    return HttpResponseRedirect(redirect_url)
