from django.contrib.auth.models import Permission
from django.contrib.auth.models import User

def create_users(number):
    for i in range(number):
        name = f'ala{i}'
        user = User.objects.create_user(name, f'{name}@example.com', 'kot')
        user.save()

create_users(10)
better_user = User.objects.create_user('Ola', 'staff@example.com', 'kot')
better_user.is_staff = True
better_user.save()

