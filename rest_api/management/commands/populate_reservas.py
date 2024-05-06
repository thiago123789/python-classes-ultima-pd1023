from django.core.management import BaseCommand
from model_bakery import baker

from base.models import ReservaModel


class Command(BaseCommand):
    help = 'Popula reservas com dados fakes'

    def handle(self, *args, **options):
        total = 50
        self.stdout.write(self.style.WARNING(f'Criar {total} reservas'))
        for i in range(total):
            reserva = baker.make(ReservaModel)
            reserva.save()

        self.stdout.write(self.style.SUCCESS(f'Reservas criadas com sucesso'))

