from pprint import pprint

from config.client import get_client
from config.constants import ARTIST_W_NAME
from config.state import State
from utils.cli import query_yes_no

yt_music = get_client()

state = State()


def map_raw_tracks_to_song_names(raw_tracks, artist_field='artists'):
    track_names_w_artist = [[
        track['title'] + " - " + ' & '.join([
            artist['name'] for artist in track[artist_field] or ARTIST_W_NAME
        ]), track['videoId']
    ] for track in raw_tracks]
    return track_names_w_artist


def get_playlist_info(id: str):
    playlist = yt_music.get_playlist(id)
    raw_tracks = playlist["tracks"]
    track_names_w_artist = map_raw_tracks_to_song_names(raw_tracks)
    return {'title': playlist['title'], 'tracks': track_names_w_artist}


playlist_id = ""

state_key = f'pl-${playlist_id}'
if state_key not in state.state:
    state.state[state_key] = get_playlist_info(playlist_id)
    state.save_state()
playlist_tracks = [track[0] for track in state.state[state_key]['tracks']]


def get_uploaded_track_info(limit=100):
    raw_tracks = yt_music.get_library_upload_songs(limit=limit)
    track_names_w_artist = map_raw_tracks_to_song_names(raw_tracks,
                                                        artist_field='artist')
    return {'tracks': track_names_w_artist}


# state_key = 'upload-tracks-3000'
# if state_key not in state.state:
#     state.state[state_key] = get_uploaded_track_info(3000)
#     state.save_state()
# upload_tracks = [track[0] for track in state.state[state_key]['tracks']]


def search_closest_uploaded_song(track):
    found_tracks = yt_music.search(track, filter='uploads')
    if len(found_tracks) == 2: return found_tracks[1]['videoId']
    if found_tracks:
        pprint([t['title'] for t in found_tracks])
        match_found = query_yes_no(
            f"Do you see a desired match for `{track}`?")
        if match_found:
            valid_choice = None
            while not valid_choice:
                try:
                    matched_idx = int(
                        input(
                            f"Enter your choice [1, ..., {len(found_tracks)}]: "
                        ))
                except Exception:
                    continue

                matched_idx -= 1
                if matched_idx < 0 or matched_idx >= len(found_tracks):
                    print("ERROR: Invalid choice entered!")
                else:
                    return found_tracks[matched_idx]['videoId']


for pl_track in playlist_tracks:
    id = search_closest_uploaded_song(pl_track)
    yt_music.add_playlist_items('', [id])
