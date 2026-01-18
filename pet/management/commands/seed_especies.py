from django.core.management.base import BaseCommand

from pet.models import Especie, Raca


class Command(BaseCommand):
    help = "Popula as tabelas Especie e Raca com dados comuns"

    def handle(self, *args, **options):
        especies_racas = {
            "Canina": [
                "Vira-lata (SRD)",
                "Labrador Retriever",
                "Golden Retriever",
                "Poodle",
                "Bulldog Francês",
                "Pastor Alemão",
                "Pinscher",
                "Shih Tzu",
                "Yorkshire Terrier",
            ],
            "Felina": [
                "Vira-lata (SRD)",
                "Siamês",
                "Persa",
                "Maine Coon",
                "Bengal",
                "Angorá",
            ],
        }

        for nome_especie, racas in especies_racas.items():
            especie, created = Especie.objects.get_or_create(
                nome=nome_especie
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Espécie criada: {nome_especie}"
                    )
                )

            for nome_raca in racas:
                raca, raca_created = Raca.objects.get_or_create(
                    especie=especie,
                    raca=nome_raca,
                )

                if raca_created:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f"  Raça criada: {nome_raca}"
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS("✔ Carga de espécies e raças finalizada.")
        )
