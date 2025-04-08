from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Test command to verify loading'

    def handle(self, *args, **kwargs):
        self.stdout.write('Test command executed successfully.')
