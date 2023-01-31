"""my_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fruits import views as views_fruits
from week_days import views as views_week

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fruits/apple', views_fruits.apple),
    path('fruits/banana', views_fruits.banana),
    path('week_days/monday', views_week.monday),
    path('week_days/tuesday', views_week.tuesday),
]
