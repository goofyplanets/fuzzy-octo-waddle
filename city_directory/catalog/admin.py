from django.contrib import admin
from .models import Country, City


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "external_id"]
    search_fields = ["name", "code", "external_id"]


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name", "country_name", "country_code"]
    list_filter = ["country"]
