from django.core.management.base import BaseCommand
from core.scripts.sync import loop_principal

class Command(BaseCommand):
    help = 'Sincroniza os dados da API de conferência em loop'

    def handle(self, *args, **kwargs):
        loop_principal()