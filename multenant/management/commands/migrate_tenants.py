from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.core.management.commands.migrate import Command as MigrateCommand

from multenant.utils import get_tenant_databases


class Command(BaseCommand):
    help = 'Migrate tenant databases'

    def handle(self, *args, **options):
        all_databases = get_tenant_databases()

        for x in all_databases.keys():
            self.stdout.write(self.style.SUCCESS(f"Running migrations for: {x}"))
            call_command('migrate', database=x)
