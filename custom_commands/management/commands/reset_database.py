"""Management команда для сброса контейнера с БД."""
import os
from time import sleep

import docker
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from docker.errors import NotFound
from docker.models.containers import Container

client = docker.from_env()


class Command(BaseCommand):
    """Класс исполняемой команды."""

    help = 'Resets current docker database'

    AVAILABLE_ARGUMENTS = [
        ('-r', '--root')
    ]

    def add_arguments(self, parser):
        """Метод для добавления аргументов команде."""
        for argument in self.AVAILABLE_ARGUMENTS:
            parser.add_argument(*argument, action='store_true', default=False,
                                help='Container name as projects upper root directory name')

    def handle(self, *args, **options):
        """Метод, отвечающий за вызов команды."""
        database = settings.DATABASES['default']
        root = options.get('root', False)
        if root is True:
            container_name = settings.BASE_DIR.split('/')[-2]
        else:
            container_name = input('Enter container name to search for reset: ')

        if database['ENGINE'] == 'django.db.backends.postgresql_psycopg2':
            try:
                container: Container = client.containers.get(container_name)
                print('Killing existing container...')
                container.kill()
                print('Removing existing container...')
                container.remove()
            except NotFound:
                pass

            database_launch_settings = {
                'POSTGRES_USER': database['USER'],
                'POSTGRES_PASSWORD': database['PASSWORD'],
                'POSTGRES_DB': database['NAME'],
            }

            container_restart_policy = {'Name': 'always'}

            ports = {'5432/tcp': database['PORT']}

            print('Starting new PostgreSQL container...')
            client.containers.run('postgres:12-alpine', name=container_name, detach=True, ports=ports,
                                  environment=database_launch_settings, restart_policy=container_restart_policy)
            sleep(2)
            print('Migrating to database...')
            try:
                call_command('migrate')
                if os.path.exists(os.path.join(settings.BASE_DIR, 'fixtures')):
                    for fixture in os.listdir(os.path.join(settings.BASE_DIR, 'fixtures')):
                        print(f'Loading fixture {fixture}...')
                        call_command('loaddata', f'fixtures/{fixture}')
                print('\n\nCompleted!')
            except Exception as exc:
                print(f'\n\nSomething went wrong during migration.\nError message: {exc}')

        else:
            print('No postgres engine configured')
