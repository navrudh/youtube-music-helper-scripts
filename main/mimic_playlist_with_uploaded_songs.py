from config.client import get_client
from config.state import State
from helpers.uploads import get_uploaded_track_info

if __name__ == '__main__':
    yt_music = get_client()
    state = State()

    dest_playlist_id = "PL8saxFz0vWFwyircqU_DLEB8XcQt0uzG_"
    last_n_songs = 12

    state_key = f'upload-tracks-{last_n_songs}'
    if state_key not in state.state:
        state.state[state_key] = get_uploaded_track_info(yt_music, last_n_songs)
        state.save_state()
    upload_tracks_ids = [track.id for track in state.state[state_key]['tracks']][:last_n_songs]

    yt_music.add_playlist_items(dest_playlist_id, upload_tracks_ids)
