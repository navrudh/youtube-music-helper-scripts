from ytmusicapi import YTMusic

from dataclazzes.playlist import Playlist
from dataclazzes.track import Track


def get_playlist_info(ytm_client: YTMusic, id: str):
    playlist = ytm_client.get_playlist(id)
    raw_tracks = playlist["tracks"]
    return Playlist(id='id',
                    title=playlist['title'],
                    tracks=Track.from_raw_tracks(raw_tracks))


def get_user_playlist_by_title(ytm_client: YTMusic,
                               title: str,
                               limit: int = 25):
    raw_playlists = ytm_client.get_library_playlists(limit=limit)
    playlists = Playlist.from_raw(raw_playlists)
    for pl in playlists:
        if pl.title is title:
            return pl


def create_playlist(ytm_client: YTMusic, title: str, desc: str = ""):
    id = ytm_client.create_playlist(title=title, description=desc)
    if not isinstance(id, str):
        print(id)
        raise Exception("Failed creating playlist!")
    return Playlist(id=id, title=title)
