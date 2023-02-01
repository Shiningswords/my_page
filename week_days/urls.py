from django.urls import path
from . import views

urlpatterns = [
    path('<all_week>/', views.get_info_about_all_week)
]
