from django.core.management import (
    BaseCommand
)


from customers.utils import (
    send_sms
)


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        send_sms(
            '+265883585906',
            'Test SMS'
        )
