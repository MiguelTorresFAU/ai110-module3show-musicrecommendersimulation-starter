# VibeRank Model Card

## Intended use

A classroom simulation for understanding how song attributes become rankings. It compares one declared profile with a small catalog.

## How it works

Matching genre earns two points and matching mood earns one point. The closer the energy is to the user's target, the more of a final point the song earns. Each result lists all three contributions. The starter's catalog-order placeholder was replaced with a real ranking.

## Data

The catalog contains 18 fictional tracks, including 10 starter tracks and eight additions. The additions include folk, ska, hip hop, drum and bass, classical, salsa, soul, and house. Genre, mood, and energy enter the score. Tempo, valence, danceability, and acousticness remain catalog metadata.

## Strengths

High-Energy Pop put Sunrise City first with 3.98 because the genre and mood match and the energy gap is 0.02. Chill Lofi placed Midnight Coding and Library Rain first and second, both matching genre and mood with small energy gaps.

## Limitations and bias

Exact labels split indie pop from pop, which can hide related artists. Chill Lofi returned three lofi songs in its top five because the genre bonus is strong and there are several lofi entries. The sad, high-energy profile ranked two pop tracks ahead of Concrete Letters, even though it was the only sad track in the top five. That illustrates how the catalog and weights can narrow discovery.

## Evaluation

The [README](README.md#sample-recommendation-output) records each top five and the weight experiment.

- Pop versus Lofi: Sunrise City leads pop, while Midnight Coding leads lofi because the desired mood and energy change along with genre.
- Pop versus Rock: Gym Hero appears in both lists. It earns genre points from Pop and mood points from Rock.
- Lofi versus Rock: lofi starts with quiet tracks around energy 0.40, while rock starts with Storm Runner at 0.91.
- Pop versus Sad: changing the desired mood and target energy moves Gym Hero above Sunrise City. Concrete Letters appears because its mood and energy fit.
- Lofi versus Sad: the former favors chill tracks near 0.40, while the latter favors pop and tracks near 0.90.
- Rock versus Sad: Gym Hero and Concrete Letters appear in both lists for different reasons. Gym Hero matches the rock profile's intense mood and the sad profile's pop genre.

Halving genre weight and doubling energy weight moved Transit Bloom from third to second and Gym Hero from second to fourth for High-Energy Pop. It better rewards a happy track with exactly the requested energy, while giving less weight to a literal pop match. There is no listener feedback to establish whether the change improves accuracy.

## Future work

Allow multiple preferred genres and compare a diversity-aware ranking against the current baseline. Add more examples for rare mood and genre combinations and test them against listener judgments.

## Engineering reflection draft

The evaluation illustrates how top-ranked results can look plausible while giving one preference more influence than expected. AI assisted with implementing the baseline and suggesting contrasting profiles. The actual CLI output provides a way to check those claims by inspecting the points and comparing rankings. The student's personal reflection can build on which of these results agreed with their musical intuition.
