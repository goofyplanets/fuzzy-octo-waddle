from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("city/", views.city_list_by_country, name="city_list_by_country"),
    path("country/top/", views.top_countries, name="top_countries"),
]
