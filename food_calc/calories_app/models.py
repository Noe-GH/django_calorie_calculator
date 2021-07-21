from django.db import models
from django.contrib.auth.models import User

class Aliment(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)
    carbs = models.FloatField()
    proteins = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

class Consumption(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    aliment = models.ForeignKey(Aliment, on_delete=models.CASCADE)
    