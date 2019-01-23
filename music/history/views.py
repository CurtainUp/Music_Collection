from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Artist
from .models import Song
from .forms import AddSong, AddArtist

# Create your views here.

# Form for adding songs to db
def add_song(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddSong(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/history/songs/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddSong()

    return render(request, 'history/addsong.html', {'form': form})

def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddArtist(request.POST)
        # check whether it's valid:
        if form.is_valid():
            artist = Artist()
            artist.artist_name = form.cleaned_data['artist_name']
            artist.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/history/artists/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddArtist()

    return render(request, 'history/addartist.html', {'form': form})

def index(request):
  return render(request, 'history/index.html')

def artists(request):
  all_artists = Artist.objects.order_by('artist_name')
  context = {'all_artists': all_artists}
  return render(request, 'history/artists.html', context)

def songs(request):
  all_songs = Song.objects.order_by('song_title')
  # artist_name = Song.artist.artist_name
  context = {'songs': all_songs}
  return render(request, 'history/songs.html', context)

def details(request, artist_id):
  songs_by_artist = Song.objects.filter(artist_id = artist_id)
  artist_name = Artist.objects.get(pk=artist_id)
  context = {'songs': songs_by_artist, 'artist_name': artist_name}
  return render(request, 'history/details.html', context)