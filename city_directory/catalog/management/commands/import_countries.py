import csv
from django.core.management.base import BaseCommand
from catalog.models import Country


class Command(BaseCommand):
    help = "Import countries from CSV. Expected headers: name and either country_id or country_code"

    def add_arguments(self, parser):
        parser.add_argument("D:\django\csv_files\cities.csv", type=str)

    def handle(self, *args, **options):
        path = options["D:\django\csv_files\cities.csv"]
        with open(path, encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            for row in reader:
                external = (
                    row.get("country_id") or row.get("countryId") or row.get("id")
                )
                name = row.get("country_name") or row.get("name")
                code = row.get("country_code") or row.get("code")

                if not external:
                    self.stdout.write(
                        self.style.WARNING(f"Пропуск строки без country_id: {row}")
                    )
                    continue
                try:
                    external = int(external)
                except ValueError:
                    self.stdout.write(
                        self.style.ERROR(f"Неверный country_id {external}")
                    )
                    continue

                obj, created = Country.objects.update_or_create(
                    external_id=external,
                    defaults={"name": name or "", "code": code or ""},
                )
                action = "Создано" if created else "Обновлено"
                self.stdout.write(f"{action} Страна: {obj}")
