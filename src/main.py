"""Run the Week 6 catalog evaluation in the terminal."""

from pathlib import Path

from .recommender import load_songs, recommend_songs

PROFILES = {
    "High-Energy Pop": {"genre": "pop", "mood": "happy", "energy": 0.8},
    "Chill Lofi": {"genre": "lofi", "mood": "chill", "energy": 0.4},
    "Intense Rock": {"genre": "rock", "mood": "intense", "energy": 0.9},
    "Sad but High-Energy": {"genre": "pop", "mood": "sad", "energy": 0.9},
}


def main() -> None:
    catalog = Path(__file__).resolve().parents[1] / "data" / "songs.csv"
    songs = load_songs(catalog)
    print(f"Loaded songs: {len(songs)}")
    for name, preferences in PROFILES.items():
        print(f"\n{name}")
        for index, (song, score, reasons) in enumerate(recommend_songs(preferences, songs), start=1):
            print(f"{index}. {song['title']} ({song['genre']}) | {score:.2f} | {reasons}")

    print("\nHigh-Energy Pop with genre halved and energy doubled")
    for index, (song, score, reasons) in enumerate(
        recommend_songs(PROFILES["High-Energy Pop"], songs, weights=(1, 1, 2)), start=1
    ):
        print(f"{index}. {song['title']} ({song['genre']}) | {score:.2f} | {reasons}")


if __name__ == "__main__":
    main()
