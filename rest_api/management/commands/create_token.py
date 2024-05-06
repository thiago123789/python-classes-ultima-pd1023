from django.core.management import BaseCommand
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token


class Command(BaseCommand):
    help = 'Create a new token using the provided credentials'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True)
        parser.add_argument('--password', required=True)

    ## --username USER_NAME --password PASSWORD
    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        self.stdout.write(
            self.style.WARNING(f'Token será criado para usuário: {username}')
        )
        user = User(username=username, password=password)
        user.first_name = username
        user.set_password(password)
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f'Usuário salvo')
        )
        self.stdout.write(
            self.style.WARNING(f'Criando token para usuário')
        )
        token = Token.objects.create(user=user)
        self.stdout.write(
            self.style.SUCCESS(f'Token {token.key}')
        )
