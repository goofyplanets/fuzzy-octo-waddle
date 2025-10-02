"""
URL configuration for city_directory project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from catalog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_page, name="home"),
    path("city/", views.city_list_by_country, name="city_list"),
    path("country/top/", views.top_countries, name="top_countries"),
]
