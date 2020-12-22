from pprint import pprint
from typing import Union, List

from ytmusicapi import YTMusic

from dataclazzes.track import Track
from utils.cli import query_yes_no


def filterResultsBy(searchResults: List[dict], resultType: str):
    return [res for res in searchResults if res['resultType'] is resultType]


def get_uploaded_track_info(ytm_client: YTMusic, limit=100):
    raw_tracks = ytm_client.get_library_upload_songs(limit=limit)
    return Track.from_raw_tracks(raw_tracks)


def find_closest_uploaded_song_by_title(ytm_client: YTMusic,
                                        track: Union[str, Track]):
    found_tracks = ytm_client.search(str(track), filter='uploads')
    found_tracks = Track.from_raw_tracks(found_tracks)
    if len(found_tracks) == 2: return found_tracks[1].id
    if found_tracks:
        pprint(found_tracks)
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


def search_uploaded_tracks(ytm_client: YTMusic, query: str, limit: int = 20):
    search_results = ytm_client.search(query, limit=limit, filter='uploads')
    raw_tracks = filterResultsBy(search_results, 'song')
    return Track.from_search_results(raw_tracks)
