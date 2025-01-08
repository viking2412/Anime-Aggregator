from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#anime info, add amount of episodes etc
class Anime(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    airing_status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.PositiveBigIntegerField(default=1)
    text = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} review on {self.anime.title}"
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the user
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)  # Link to the anime
    status = models.CharField(
        max_length=20,
        choices=[('watching', 'Watching'), ('completed', 'Completed'), ('to_watch', 'To Watch')],
        default='to_watch'
    )

    def __str__(self):
        return f"{self.user.username}'s Watchlist: {self.anime.title} ({self.status})"
