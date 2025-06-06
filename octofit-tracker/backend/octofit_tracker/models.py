from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    # Add additional fields as needed
    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)
    # Add additional fields as needed
    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    duration = models.IntegerField()  # in minutes
    date = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    # Add additional fields as needed

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=50)
    details = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Add additional fields as needed
