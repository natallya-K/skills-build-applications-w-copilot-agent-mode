from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Minimal command to test detection'

    def handle(self, *args, **kwargs):
        self.stdout.write('Minimal command executed successfully.')
