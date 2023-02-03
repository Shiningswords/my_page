from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('type/', views.types),
    path('type/<str:type_fruits>/', views.types_f, name='type_f'),
    path('<int:all_fruits>/', views.get_info_about_all_fruits_by_num),
    path('<str:all_fruits>/', views.get_info_about_all_fruits, name='fruits-name')

]
