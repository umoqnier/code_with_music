from django.db import models


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    track_num = models.IntegerField()
    composer = models.CharField(max_length=100)
    score = models.DecimalField(decimal_places=2, max_digits=3)
    file = models.FileField()

    def __str__(self):
        return "%d: $s" % self.id, self.name
