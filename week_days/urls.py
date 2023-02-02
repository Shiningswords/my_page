from django.urls import path
from . import views

urlpatterns = [
    path('<int:all_week>/', views.get_info_about_all_week),
    path('<str:all_week>/', views.get_info_about_all_week_str)
]
