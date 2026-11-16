# Music Recommender Simulation

VibeRank ranks a small catalog against an explicit taste profile and explains each result. Run it with Python 3.10 or later from the repository root.

```sh
python -m src.main
python -m pip install -r requirements.txt
python -m pytest -q
```

## How The System Works

Content-based filtering compares a track’s attributes with a listener’s preferences. Collaborative filtering uses behavior across listeners, such as shared likes or skips. This simulation uses the content-based approach because the catalog contains track metadata and no listening history.

The profile contains a desired genre, mood, and energy from 0 to 1. The program gives 2 points for a genre match, 1 for a mood match, and up to 1 for energy similarity. Energy similarity is one minus the absolute difference from the target. It sorts by total score, breaks ties by ascending catalog ID, and prints the top five along with the score contributions. Exact genre matching can overweight familiar labels and reduce discovery. See the [Model Card](model_card.md) for the observed effect.
 
## Sample Recommendation Output

```text
Loaded songs: 18

High-Energy Pop
1. Sunrise City (pop) | 3.98 | genre match (+2.00); mood match (+1.00); energy gap 0.02 (+0.98)
2. Gym Hero (pop) | 2.87 | genre match (+2.00); mood differs (+0.00); energy gap 0.13 (+0.87)
3. Transit Bloom (house) | 2.00 | genre differs (+0.00); mood match (+1.00); energy gap 0.00 (+1.00)
4. Rooftop Lights (indie pop) | 1.96 | genre differs (+0.00); mood match (+1.00); energy gap 0.04 (+0.96)
5. Market at Dusk (salsa) | 0.97 | genre differs (+0.00); mood differs (+0.00); energy gap 0.03 (+0.97)

Chill Lofi
1. Midnight Coding (lofi) | 3.98 | genre match (+2.00); mood match (+1.00); energy gap 0.02 (+0.98)
2. Library Rain (lofi) | 3.95 | genre match (+2.00); mood match (+1.00); energy gap 0.05 (+0.95)
3. Focus Flow (lofi) | 3.00 | genre match (+2.00); mood differs (+0.00); energy gap 0.00 (+1.00)
4. Spacewalk Thoughts (ambient) | 1.88 | genre differs (+0.00); mood match (+1.00); energy gap 0.12 (+0.88)
5. Coffee Shop Stories (jazz) | 0.97 | genre differs (+0.00); mood differs (+0.00); energy gap 0.03 (+0.97)

Intense Rock
1. Storm Runner (rock) | 3.99 | genre match (+2.00); mood match (+1.00); energy gap 0.01 (+0.99)
2. Gym Hero (pop) | 1.97 | genre differs (+0.00); mood match (+1.00); energy gap 0.03 (+0.97)
3. Concrete Letters (hip hop) | 0.98 | genre differs (+0.00); mood differs (+0.00); energy gap 0.02 (+0.98)
4. Brass on Canal (ska) | 0.96 | genre differs (+0.00); mood differs (+0.00); energy gap 0.04 (+0.96)
5. Signal in Blue (drum and bass) | 0.94 | genre differs (+0.00); mood differs (+0.00); energy gap 0.06 (+0.94)

Sad but High-Energy
1. Gym Hero (pop) | 2.97 | genre match (+2.00); mood differs (+0.00); energy gap 0.03 (+0.97)
2. Sunrise City (pop) | 2.92 | genre match (+2.00); mood differs (+0.00); energy gap 0.08 (+0.92)
3. Concrete Letters (hip hop) | 1.98 | genre differs (+0.00); mood match (+1.00); energy gap 0.02 (+0.98)
4. Storm Runner (rock) | 0.99 | genre differs (+0.00); mood differs (+0.00); energy gap 0.01 (+0.99)
5. Brass on Canal (ska) | 0.96 | genre differs (+0.00); mood differs (+0.00); energy gap 0.04 (+0.96)

High-Energy Pop with genre halved and energy doubled
1. Sunrise City (pop) | 3.96 | genre match (+1.00); mood match (+1.00); energy gap 0.02 (+1.96)
2. Transit Bloom (house) | 3.00 | genre differs (+0.00); mood match (+1.00); energy gap 0.00 (+2.00)
3. Rooftop Lights (indie pop) | 2.92 | genre differs (+0.00); mood match (+1.00); energy gap 0.04 (+1.92)
4. Gym Hero (pop) | 2.74 | genre match (+1.00); mood differs (+0.00); energy gap 0.13 (+1.74)
5. Market at Dusk (salsa) | 1.94 | genre differs (+0.00); mood differs (+0.00); energy gap 0.03 (+1.94)

```
