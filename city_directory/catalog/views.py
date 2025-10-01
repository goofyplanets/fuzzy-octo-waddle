from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Country
from django.db.models import Count


def city_list_by_country(request):
    country_name = request.GET.get("country", "").strip()

    if not country_name:
        return HttpResponse(
            "<h1>Please specify a country</h1>"
            "<p>Usage: /city/?country=CountryName</p>"
            "<p>Example: /city/?country=Afghanistan</p>"
        )

    cities = City.objects.filter(country__name__iexact=country_name)

    if not cities.exists():
        return HttpResponse(f"<h1>Country '{country_name}' not found</h1>")

    country = cities.first().country

    return render(
        request, "catalog/city_list.html", {"cities": cities, "country": country}
    )


def top_countries(request):
    top_countries = Country.objects.annotate(city_count=Count("cities")).order_by(
        "-city_count"
    )[:10]

    total_countries = Country.objects.count()
    total_cities = City.objects.count()

    return render(
        request,
        "catalog/top_countries.html",
        {
            "top_countries": top_countries,
            "total_countries": total_countries,
            "total_cities": total_cities,
        },
    )
