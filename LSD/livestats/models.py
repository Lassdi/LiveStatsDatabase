from django.db import models
from django.utils import timezone
import datetime

class Player(models.Model):
    name = models.CharField(max_length=20)
    joined = models.DateTimeField("Player joined")

    def __str__(self):
        return self.name
    
    def NewPlayer(self):
        return self.joined >= timezone.now() - datetime.timedelta(weeks=1)

class PlayerDescription(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    votes = models.ImageField(default=0)

    def __str__(self):
        return self.description