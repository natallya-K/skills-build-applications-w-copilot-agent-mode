from django.core.management.base import BaseCommand
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

print("populate_db.py is loaded")

print("Debug: Command class is defined and ready.")

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Populate users
        for user_data in test_users:
            User.objects.create(**user_data)

        # Populate teams
        for team_data in test_teams:
            Team.objects.create(**team_data)

        # Populate activities
        for activity_data in test_activities:
            Activity.objects.create(**activity_data)

        # Populate leaderboard
        for leaderboard_data in test_leaderboard:
            Leaderboard.objects.create(**leaderboard_data)

        # Populate workouts
        for workout_data in test_workouts:
            Workout.objects.create(**workout_data)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
