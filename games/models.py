from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GameScore(models.Model):
    GAME_CHOICES = [
        ('snake', 'Snake'),
        ('wordle', 'Wordle'),
        ('dots', 'Dots & Boxes'),
    ]
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.CharField(max_length=10, choices=GAME_CHOICES)
    score = models.IntegerField()
    date_played = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} - {self.game}: {self.score}"