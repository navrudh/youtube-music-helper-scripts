from ytmusicapi import YTMusic

from utils.mapper import map_raw_tracks_to_song_names


def get_playlist_info(ytm_client: YTMusic, id: str):
    playlist = ytm_client.get_playlist(id)
    raw_tracks = playlist["tracks"]
    track_names_w_artist = map_raw_tracks_to_song_names(raw_tracks)
    return {'title': playlist['title'], 'tracks': track_names_w_artist}
