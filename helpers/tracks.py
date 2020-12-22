from ytmusicapi import YTMusic

from dataclazzes.playlist import Playlist
from dataclazzes.track import Track


def get_playlist_info(track: YTMusic, id: str):
    playlist = ytm_client.get_playlist(id)
    raw_tracks = playlist["tracks"]
    return Playlist(id='id',
                    title=playlist['title'],
                    tracks=Track.from_raw_tracks(raw_tracks))
