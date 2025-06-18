from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Ensure related objects are saved before creating dependent entries 
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password456")

        team1 = Team.objects.create(name="Team Alpha", members=["John Doe", "Jane Smith"])
        team2 = Team.objects.create(name="Team Beta", members=["Alice", "Bob"])

        Activity.objects.create(user=user1, type="Running", duration=30)
        Activity.objects.create(user=user2, type="Cycling", duration=45)

        Leaderboard.objects.create(team=team1, points=100)
        Leaderboard.objects.create(team=team2, points=80)

        Workout.objects.create(name="Morning Run", description="A quick morning run to start the day.")
        Workout.objects.create(name="Evening Yoga", description="Relaxing yoga session in the evening.")

        self.stdout.write(self.style.SUCCESS('Test data populated successfully'))
