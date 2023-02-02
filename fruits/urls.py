from django.urls import path
from . import views

urlpatterns = [
    path('<int:all_fruits>/', views.get_info_about_all_fruits_by_num),
    path('<str:all_fruits>/', views.get_info_about_all_fruits)

]
