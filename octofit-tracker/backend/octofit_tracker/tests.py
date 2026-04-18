from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Test Team", description="A test team")
        self.assertEqual(str(team), "Test Team")

class UserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name="Test Team2")
        user = User.objects.create(name="Alice", email="alice@example.com", team=team)
        self.assertEqual(str(user), "Alice")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name="Test Team3")
        user = User.objects.create(name="Bob", email="bob@example.com", team=team)
        activity = Activity.objects.create(user=user, activity_type="Run", duration_minutes=30, date=timezone.now().date())
        self.assertIn("Run", str(activity))

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        team = Team.objects.create(name="Test Team4")
        workout = Workout.objects.create(name="Pushups", description="Do 20 pushups", suggested_for_team=team)
        self.assertEqual(str(workout), "Pushups")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Test Team5")
        leaderboard = Leaderboard.objects.create(team=team, total_points=100)
        self.assertIn("Test Team5", str(leaderboard))
