from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class DietEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    meal = models.CharField(max_length=255)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.meal} - {self.calories} cal"
