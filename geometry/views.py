from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi
from django.urls import reverse


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {pi * radius ** 2}')


def get_rectangle_area_get(request, width: int, height: int):
    redirected_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirected_url)


def get_square_area_get(request, width: int):
    redirected_url = reverse('square-name', args=(width,))
    return HttpResponseRedirect(redirected_url)


def get_circle_area_get(request, radius: int):
    redirected_url = reverse('circle-name', args=(radius,))
    return HttpResponseRedirect(redirected_url)
