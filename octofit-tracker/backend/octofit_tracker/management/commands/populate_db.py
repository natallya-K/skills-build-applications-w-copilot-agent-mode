from django.core.management.base import BaseCommand

print("populate_db.py is loaded")

print("Debug: Command class is defined and ready.")

class Command(BaseCommand):
    help = 'Test command to verify loading'

    def handle(self, *args, **kwargs):
        self.stdout.write('Test command executed successfully.')
