# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process      Use this to change PS scope
# spotify-env\Scripts\activate.ps1                                      Use this to activate the virtualenv

# Imports other files
import input
import output
import logic


# Saves playlists for later, raw links work fine
input_playlist = ''
output_playlist  = ''


# Gets required input and passes it through logic function
artist_uris = [input.tracks_by_artist(input_playlist, '5 Seconds of Summer'), input.tracks_by_artist(input_playlist, 'Taylor Swift'), input.tracks_by_artist(input_playlist, 'One Direction')]
uri_list = logic.individual_weightings(artist_uris, [1, 1, 1])
all_uris = input.all_tracks(input_playlist)


# Outputs the playlist
# output.replace_playlist(output_playlist, uri_list)
# output.replace_playlist(output_playlist, all_uris)

print(input.tracks_by_artist(input_playlist, '5 Seconds of Summer'))