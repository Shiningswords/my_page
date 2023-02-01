from django.urls import path
from . import views

urlpatterns = [
    path('apple/', views.apple),
    path('banana/', views.banana)
]
