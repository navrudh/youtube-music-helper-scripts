from dataclasses import dataclass

from dataclazzes.track import Track


@dataclass
class Playlist:
    """Class for storing playlist information."""
    id: str
    title: str
    tracks: [Track]
