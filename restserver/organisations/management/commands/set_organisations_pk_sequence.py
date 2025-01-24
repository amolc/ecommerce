from typing import (
    Any,
)
from django.core.management.base import (  # type: ignore
    BaseCommand,
)
from django.db import (  # type: ignore
    connection,
)
from organisations.models import (
    Organisation,
)

class Command(BaseCommand):
    help = 'Set the primary key sequence to start from the current max(id) for organisations app'

    def handle(self, *args: Any, **kwargs: Any):
        with connection.cursor() as cursor:
            for model in [Organisation,]:
                table_name = model._meta.db_table
                cursor.execute(f"SELECT setval(pg_get_serial_sequence('{table_name}', 'id'), coalesce(max(id), 1), max(id) IS NOT null) FROM {table_name};")
                self.stdout.write(self.style.SUCCESS(f'Successfully set primary key sequence for {table_name}'))
