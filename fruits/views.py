from django.shortcuts import render
from django.http import HttpResponse


def apple(request):
    return HttpResponse('Яблоко')


def banana(request):
    return HttpResponse('Банан')
