import csv
from django.core.management.base import BaseCommand
from catalog.models import City, Country


class Command(BaseCommand):
    help = "Import cities from CSV."

    def add_arguments(self, parser):
        parser.add_argument("D:\django\csv_files\cities.csv", type=str)
        parser.add_argument(
            "--country-by",
            choices=["id", "code"],
            default="id",
            help="how to match city rows to countries: id (default) or code",
        )

    def handle(self, *args, **options):
        path = options["D:\django\csv_files\cities.csv"]
        country_by = options["country_by"]

        with open(path, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                city_name = row.get("name")
                if not city_name:
                    self.stdout.write(
                        self.style.WARNING(f"Skipping row without name: {row}")
                    )
                    continue

                country = None
                if country_by == "id":
                    cid = (
                        row.get("country_id")
                        or row.get("countryId")
                        or row.get("country_external_id")
                    )
                    if not cid:
                        self.stdout.write(
                            self.style.WARNING(
                                f"No country_id for city '{city_name}', skipping"
                            )
                        )
                        continue
                    try:
                        country = Country.objects.get(external_id=int(cid))
                    except Country.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Country with external_id={cid} not found for city '{city_name}'"
                            )
                        )
                        continue
                else:
                    ccode = (
                        row.get("country_code")
                        or row.get("countryCode")
                        or row.get("country")
                    )
                    if not ccode:
                        self.stdout.write(
                            self.style.WARNING(
                                f"No country_code for city '{city_name}', skipping"
                            )
                        )
                        continue
                    try:
                        country = Country.objects.get(code=ccode)
                    except Country.DoesNotExist:
                        self.stdout.write(
                            self.style.ERROR(
                                f"Country with code='{ccode}' not found for city '{city_name}'"
                            )
                        )
                        continue

                city, created = City.objects.update_or_create(
                    name=city_name, country=country
                )
                action = "Created" if created else "Updated"
                self.stdout.write(f"{action} City: {city}")
