from django.db import models

# Create your models here.

# Build a model representing your Artist table.
# Build a model representing your Song table. Ensure that you define the foreign key to the artist table.

class Artist(models.Model):
  artist_name = models.CharField(max_length=200)

  def __str__(self):
        return self.artist_name

class Song(models.Model):
  # defines the artist table as the foreign key for the song table. Will delete song if artist is deleted via CASCADE
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  song_title = models.CharField(max_length=200)

  def __str__(self):
        return self.song_title
