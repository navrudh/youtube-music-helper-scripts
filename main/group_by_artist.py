from config.client import get_client
from helpers.playlists import get_user_playlist_by_title, create_playlist
from helpers.uploads import search_uploaded_tracks

if __name__ == '__main__':
    yt_music = get_client()
    artist_name = "Streex"
    playlist_name = f"{artist_name} (Generated Playlist)"
    playlist = get_user_playlist_by_title(yt_music, playlist_name, limit=100)
    if not playlist:
        playlist = create_playlist(yt_music, title=playlist_name)
    tracks = search_uploaded_tracks(yt_music, artist_name, limit=70)
    track_ids = [tr.id for tr in tracks]
    yt_music.add_playlist_items(playlist.id, track_ids)
