from config.client import get_client
from config.state import State
from helpers.playlists import get_playlist_info
from helpers.uploads import find_closest_uploaded_song_by_title, get_uploaded_track_info

if __name__ == '__main__':
    yt_music = get_client()
    state = State()

    src_playlist_id = ""
    dest_playlist_id = ""

    state_key = f'pl-${src_playlist_id}'
    if state_key not in state.state:
        state.state[state_key] = get_playlist_info(yt_music, src_playlist_id)
        state.save_state()
    playlist_tracks = [
        str(track) for track in state.state[state_key]['tracks']
    ]

    state_key = 'upload-tracks-3000'
    if state_key not in state.state:
        state.state[state_key] = get_uploaded_track_info(yt_music, 3000)
        state.save_state()
    upload_tracks = [str(track) for track in state.state[state_key]['tracks']]

    for pl_track in playlist_tracks:
        id = find_closest_uploaded_song_by_title(yt_music, pl_track)
        yt_music.add_playlist_items(dest_playlist_id, [id])
