from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='test1@test1.com',
            username='None',
            first_name='test1',
            last_name='test1',
        )

        user.set_password('1234')
        user.is_staff = True
        # user.is_superuser = True
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Пользователь {user.first_name} {user.last_name} создан!'))
