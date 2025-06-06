from django.test import TestCase
from tracker.models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="testpass")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create(email="team@example.com", name="Team User", password="testpass")
        team = Team.objects.create(name="Team A")
        team.members.add(user)
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="activity@example.com", name="Activity User", password="testpass")
        activity = Activity.objects.create(user=user, activity_type="run", duration=30)
        self.assertEqual(activity.activity_type, "run")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Leaderboard Team")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="workout@example.com", name="Workout User", password="testpass")
        workout = Workout.objects.create(user=user, workout_type="cardio", details="30 min run")
        self.assertEqual(workout.workout_type, "cardio")
