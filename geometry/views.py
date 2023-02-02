from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from math import pi


def get_rectangle_area(request, width: int, height: int):
    return HttpResponse(f'Площадь прямоугольника размером {width}x{height} равна {width * height}')


def get_square_area(request, width: int):
    return HttpResponse(f'Площадь квадрата размером {width}x{width} равна {width * width}')


def get_circle_area(request, radius: int):
    return HttpResponse(f'Площадь круга радиусом {radius} равна {pi * radius ** 2}')


def get_rectangle_area_get(request, width: int, height: int):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}/')


def get_square_area_get(request, width: int):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}/')


def get_circle_area_get(request, radius: int):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}/')
