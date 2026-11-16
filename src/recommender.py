import csv
from dataclasses import asdict, dataclass

DEFAULT_WEIGHTS = (2.0, 1.0, 1.0)

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """Provide the same ranking through the starter's object interface."""

    def __init__(self, songs: list[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> list[Song]:
        ranked = recommend_songs(self._preferences(user), [asdict(song) for song in self.songs], k)
        return [Song(**song) for song, _, _ in ranked]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        _, reasons = score_song(self._preferences(user), asdict(song))
        return "; ".join(reasons)

    @staticmethod
    def _preferences(user: UserProfile) -> dict:
        return {"genre": user.favorite_genre, "mood": user.favorite_mood, "energy": user.target_energy}


def load_songs(csv_path: str) -> list[dict]:
    """Load the catalog and convert numeric features to numbers."""
    with open(csv_path, newline="", encoding="utf-8") as source:
        songs = list(csv.DictReader(source))
    for song in songs:
        song["id"] = int(song["id"])
        for field in ("energy", "tempo_bpm", "valence", "danceability", "acousticness"):
            song[field] = float(song[field])
        if not 0.0 <= song["energy"] <= 1.0:
            raise ValueError(f"Song {song['id']} has energy outside [0, 1]")
    return songs


def score_song(user_prefs: dict, song: dict, *, weights=DEFAULT_WEIGHTS) -> tuple[float, list[str]]:
    """Return the weighted score and a reason for each contribution."""
    target = user_prefs["energy"]
    if not 0.0 <= target <= 1.0:
        raise ValueError("Target energy must be between 0 and 1")
    genre_weight, mood_weight, energy_weight = weights
    genre_match = user_prefs["genre"].strip().casefold() == song["genre"].strip().casefold()
    mood_match = user_prefs["mood"].strip().casefold() == song["mood"].strip().casefold()
    gap = abs(song["energy"] - target)
    genre_points = genre_weight if genre_match else 0.0
    mood_points = mood_weight if mood_match else 0.0
    energy_points = energy_weight * (1 - gap)
    reasons = [
        f"genre {'match' if genre_match else 'differs'} (+{genre_points:.2f})",
        f"mood {'match' if mood_match else 'differs'} (+{mood_points:.2f})",
        f"energy gap {gap:.2f} (+{energy_points:.2f})",
    ]
    return round(genre_points + mood_points + energy_points, 10), reasons


def recommend_songs(user_prefs: dict, songs: list[dict], k: int = 5, *, weights=DEFAULT_WEIGHTS) -> list[tuple[dict, float, str]]:
    """Rank every song by score, breaking ties by catalog ID."""
    ranked = []
    for song in songs:
        score, reasons = score_song(user_prefs, song, weights=weights)
        ranked.append((song, score, "; ".join(reasons)))
    ranked.sort(key=lambda item: (-item[1], item[0]["id"]))
    return ranked[:max(0, k)]
