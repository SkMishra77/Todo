# custom_commands/management/commands/create_app.py
import os

from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create a Django app with specified name and add urls.py and serializers.py'

    def add_arguments(self, parser):
        parser.add_argument('app_name', type=str, help='Name of the app to be created')

    def handle(self, *args, **options):
        app_name = options['app_name']
        print(app_name)

        # Create the app
        call_command('startapp', app_name)

        # Create urls.py
        urls_path = os.path.join(app_name, 'urls.py')
        with open(urls_path, 'w') as urls_file:
            urls_file.write('''
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = []
urlpatterns += router.urls
''')

        self.stdout.write(self.style.SUCCESS(f'Successfully created {urls_path}'))

        # Create serializers.py
        serializers_path = os.path.join(app_name, 'serializers.py')
        with open(serializers_path, 'w') as serializers_file:
            serializers_file.write("from rest_framework import serializers\n\n# Add your serializers here\n")

        self.stdout.write(self.style.SUCCESS(f'Successfully created {serializers_path}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created app: {app_name}'))
