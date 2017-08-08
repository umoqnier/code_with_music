from django.db import models
from modules.songs.models import Song


class Album(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    year = models.DateField()
    score = models.DecimalField(decimal_places=2, max_digits=3)
    songs = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='songs')
    cover = models.ImageField()


    def __str__(self):
        return "%d: %s" % self.id, self.name