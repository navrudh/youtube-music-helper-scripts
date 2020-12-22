from dataclasses import dataclass

from config.constants import ARTIST_W_NAME


@dataclass
class Track:
    """Class for storing track information."""
    id: str
    title: str
    artist: str

    def __str__(self):
        return self.title + " - " + self.artist

    @staticmethod
    def from_raw_tracks(raw_tracks, artist_field='artists'):
        return [Track(id=track['videoId'],
                      title=track['title'],
                      artist=' & '.join([
                          artist['name'] for artist in track[artist_field] or ARTIST_W_NAME
                      ])) for track in raw_tracks]
