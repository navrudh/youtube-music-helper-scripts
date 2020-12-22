from dataclasses import dataclass, field

from dataclazzes.track import Track


@dataclass
class Playlist:
    """Class for storing playlist information."""
    id: str
    title: str
    tracks: [Track] = field(default_factory=list)

    @staticmethod
    def from_raw(raw_playlists: list):
        return [
            Playlist(id=playlist['playlistId'], title=playlist['title'])
            for playlist in raw_playlists
        ]
