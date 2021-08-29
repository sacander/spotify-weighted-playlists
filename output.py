# Imports spotipy libraries
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Imports credentials
import cred 

# Imports math
import math

# Defines scope and create spotify object
scope = ['user-modify-playback-state, playlist-modify-private', 'playlist-modify-public']
spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))


# Separates uri list into 100 uri segments to bypass 100 track limit
def segment_100(list): # list takes a single list

    segmented_list = []

    for x in range(math.ceil(len(list)/100)): # Finds how many sublists of length 100 are needed
        segmented_list.append(list[100*x : 100*(x+1)]) # Takes a sublist that is a multiple of 0 to 99 and adds it to a new list

    return segmented_list


# Replaces playlist with specified tracks
def replace_playlist(playlist, uri_list): # playlist takes url, uri_list takes a list of uris

    segmented_list = segment_100(uri_list) # Bypasses 100 track limit

    spotify.playlist_replace_items(playlist, segmented_list[0]) # Replaces output playlist with first 100 tracks

    for x in range(1, len(segmented_list)):
        spotify.playlist_add_items(playlist, segmented_list[x]) # Adds remaining tracks 100 at a time