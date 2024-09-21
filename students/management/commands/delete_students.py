from django.core.management.base import BaseCommand
from django.core.management import call_command
from students.models import Student, Group


class Command(BaseCommand):
    help = 'Load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Student.objects.all().delete()
        Group.objects.all().delete()
