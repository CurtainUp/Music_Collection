from django import forms
from django.forms import ModelForm

class AddSong(forms.Form):
    song_title = forms.CharField(label="Song Title", max_length=100)

class AddArtist(forms.Form):
    # class Meta:
    #   model = Artist
    artist_name = forms.CharField(label="Artist Name", max_length=100)