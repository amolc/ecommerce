from typing import Any
from argparse import ArgumentParser
from django.core.management.base import BaseCommand, CommandError
from orders.tasks import send_mail

class Command(BaseCommand):
    help = 'Send a test email'

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument('recipient', type=str, help='The recipient of the email')
        parser.add_argument('--body', type=str, default='This is a test email.', help='The body of the email')

    def handle(self, *args: Any, **options: Any) -> None:
        recipient = options['recipient']
        body_content = options['body']
        subject = 'Test Email'

        body = f"""
        <html>
        <head>
            <style>
                .header {{
                    font-size: 24px;
                    font-weight: bold;
                    color: green;
                }}
                .content {{
                    margin-top: 20px;
                }}
            </style>
        </head>
        <body>
            <p class="header">Test Email</p>
            <div class="content">
                <p>{body_content}</p>
            </div>
            <p>Best regards,</p>
            <p>Pamosapicks</p>
        </body>
        </html>
        """

        try:
            send_mail(recipient, subject, body)
            self.stdout.write(self.style.SUCCESS(f'Successfully sent email to {recipient}'))
        except Exception as e:
            raise CommandError(f'Error sending email: {e}')
