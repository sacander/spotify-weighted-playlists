# Imports spotipy libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Imports credentials
import cred 

# Imports math
import math


# Defines scope and create spotify object
scope = []
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))


# Creates track class for easy data management
class Track:
    def __init__(self, name, uri, album, artists):
        self.name = name
        self.uri = uri
        self.album = album
        self.artists = artists

# Creates list of custom track objects from input playlist, bypassing 100 track limit
def create_track_list(playlist):

    track_list = []

    for x in range(math.ceil(spotify.playlist_tracks(playlist)['total']/100)): # Finds how many sublists of length 100 are needed
        track_list.extend(get_track_list(playlist, 100*x)) # Takes a sublist and extends it onto the track list

    return track_list


# Gets list of custom track objects from input playlist with 100 track limit
def get_track_list(playlist, offset): # playlist takes url

    track_list = []

    for track in spotify.playlist_tracks(playlist, offset=offset)['items']: # Spotify returns {"items" : [{track 1}, {track 2}...]}

        try:
            name = track['track']['name'] # {track 1} = {"track" : {"name" : name}}
            uri = track['track']['uri'] # {track 1} = {"track" : {"uri" : uri}}
            album = track['track']['album']['name'] # {track 1} = {"track" : {"album" : {"name" : name}}}
            raw_artists = track['track']['artists'] # {track 1} = {"track" : {"artists" : [{artist 1}, {artist 2}...}]}}

            artists = []
            for x in raw_artists: # {artist 1} = {"name" : name}
                artists.append(x['name'])
            
            track_list.append(Track(name, uri, album, artists))

        except: # Script will crash if there's a playlist with an empty track objects, this skips any such tracks
            continue

    return track_list


# Returns list of all uris
def all_tracks(playlist): # playlist takes url

    all_tracks = []

    for track in create_track_list(playlist): # Iterates through each custom track object (made from above function) from a playlist
        all_tracks.append(track.uri)

    return all_tracks

# Returns list of track uris by specific artist
def tracks_by_artist(playlist, artist): # playlist takes url, artist takes a string

    tracks_by_artist = []

    for track in create_track_list(playlist): # Iterates through each custom track object (made from above function) from a playlist

        if (artist in track.artists): # Checks if artist is in the list of artists attribute associated with each object
            tracks_by_artist.append(track.uri)

    return tracks_by_artist