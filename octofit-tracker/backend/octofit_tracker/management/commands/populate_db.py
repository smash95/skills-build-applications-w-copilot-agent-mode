from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Deleting old data...'))
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Creating teams...'))
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        self.stdout.write(self.style.SUCCESS('Creating users...'))
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc, is_superhero=True),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True),
        ]

        self.stdout.write(self.style.SUCCESS('Creating activities...'))
        Activity.objects.create(user=users[0], activity_type='Web Swinging', duration_minutes=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], activity_type='Suit Training', duration_minutes=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], activity_type='Lasso Practice', duration_minutes=40, date=timezone.now().date())
        Activity.objects.create(user=users[3], activity_type='Martial Arts', duration_minutes=50, date=timezone.now().date())

        self.stdout.write(self.style.SUCCESS('Creating workouts...'))
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes', suggested_for_team=marvel)
        Workout.objects.create(name='Justice Jog', description='Endurance for justice', suggested_for_team=dc)

        self.stdout.write(self.style.SUCCESS('Creating leaderboards...'))
        Leaderboard.objects.create(team=marvel, total_points=100)
        Leaderboard.objects.create(team=dc, total_points=90)

        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
