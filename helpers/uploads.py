from pprint import pprint

from ytmusicapi import YTMusic

from utils.cli import query_yes_no
from utils.mapper import map_raw_tracks_to_song_names


def get_uploaded_track_info(ytm_client: YTMusic, limit=100):
    raw_tracks = ytm_client.get_library_upload_songs(limit=limit)
    track_names_w_artist = map_raw_tracks_to_song_names(raw_tracks,
                                                        artist_field='artist')
    return {'tracks': track_names_w_artist}


def search_closest_uploaded_song(ytm_client: YTMusic, track):
    found_tracks = ytm_client.search(track, filter='uploads')
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
