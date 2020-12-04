from config.constants import ARTIST_W_NAME


def map_raw_tracks_to_song_names(raw_tracks, artist_field='artists'):
    track_names_w_artist = [[
        track['title'] + " - " + ' & '.join([
            artist['name'] for artist in track[artist_field] or ARTIST_W_NAME
        ]), track['videoId']
    ] for track in raw_tracks]
    return track_names_w_artist