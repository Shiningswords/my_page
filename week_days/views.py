from django.shortcuts import render
from django.http import HttpResponse


def monday(request):
    return HttpResponse('1. Выучить Python\n2.Выучить SQL')


def tuesday(request):
    return HttpResponse('1. Выучить Django\n2.Profit')
