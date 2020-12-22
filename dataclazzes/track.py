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
    def from_raw_tracks(raw_tracks: list):
        artist_field = None

        if len(raw_tracks) != 0:
            artist_field_candidates = ['artists', 'artist']
            for field in artist_field_candidates:
                if field in raw_tracks[0].keys():
                    artist_field = field
            if not artist_field:
                raise Exception("Unable to guess artist field! Found: " +
                                str(raw_tracks[0].keys()))

        return [
            Track(id=track['videoId'],
                  title=track['title'],
                  artist=' & '.join([
                      artist['name']
                      for artist in track[artist_field] or ARTIST_W_NAME
                  ])) for track in raw_tracks
        ]
