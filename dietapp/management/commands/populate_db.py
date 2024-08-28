from django.core.management.base import BaseCommand
from dietapp.models import DietEntry, UserProfile
from django.contrib.auth.models import User
from faker import Faker  # Using Faker for generating dummy data

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('--users', type=int, default=1, help='Number of users to create')
        parser.add_argument('--records', type=int, default=1, help='Number of diet records per user')

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_users = kwargs['users']
        num_records = kwargs['records']

        for _ in range(num_users):
            # Create a dummy user
            username = fake.user_name()
            user = User.objects.create_user(username=username, password='password123')
            profile = UserProfile.objects.create(
                user=user, height=fake.random_int(min=150, max=200), 
                weight=fake.random_int(min=50, max=100), 
                age=fake.random_int(min=18, max=80)
            )

            # Create diet records for each user
            for _ in range(num_records):
                DietEntry.objects.create(
                    user=user,
                    date=fake.date_this_year(),
                    meal=fake.random_element(elements=('Breakfast', 'Lunch', 'Dinner')),
                    calories=fake.random_int(min=200, max=1000)
                )

        self.stdout.write(self.style.SUCCESS(f'Database populated with {num_users} users and {num_users * num_records} diet records.'))
