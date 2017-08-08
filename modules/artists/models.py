from django.db import models
from modules.albums.models import Album

GENDERS = (
    ('EL', 'Electronic'),
    ('PR', 'Progressive'),
    ('JZ', 'Jazz'),
    ('MT', 'Metal'),
    ('BL', 'Blues'),
    ('PO', 'Pop'),
    ('LT', 'Latin'),
    ('CL', 'Classical'),
)


class Artist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=10, choices=GENDERS)
    biography = models.TextField()
    age = models.IntegerField()
    is_alive = models.BooleanField(default=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)


    def __str__(self):
        return "%s %s" % self.name, self.last_name