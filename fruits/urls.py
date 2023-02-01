from django.urls import path
from . import views

urlpatterns = [
    path('<all_fruits>/', views.get_info_about_all_fruits)
]
