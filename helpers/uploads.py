from pprint import pprint
from typing import Union

from ytmusicapi import YTMusic

from dataclazzes.track import Track
from utils.cli import query_yes_no


def get_uploaded_track_info(ytm_client: YTMusic, limit=100):
    raw_tracks = ytm_client.get_library_upload_songs(limit=limit)
    return Track.from_raw_tracks(raw_tracks, artist_field='artist')


def search_closest_uploaded_song(ytm_client: YTMusic, track: Union[str, Track]):
    found_tracks = ytm_client.search(str(track), filter='uploads')
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
