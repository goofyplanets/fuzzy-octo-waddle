from django.contrib import admin
from .models import Country, City


class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "external_id"]
    search_fields = ["name", "code", "external_id"]


class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name", "country_name", "country_code"]
    list_filter = ["country"]


admin.site.register(City, CityAdmin)
admin.site.register(Country, CountryAdmin)
