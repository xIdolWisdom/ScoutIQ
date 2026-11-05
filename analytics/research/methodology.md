# ScoutIQ Analytics — Research Methodology

## 1. Research Scope

ScoutIQ Analytics is a descriptive soccer scouting research
project examining passing progression, passing accuracy,
and passing volume among eligible midfielders.

The frozen Passing Index V2 research population includes:

- Premier League 2015/16: 98 player-club profiles
- La Liga 2015/16: 102 player-club profiles
- Total: 200 player-club profiles across 40 clubs

Scores and rankings are calculated separately by league.
Scores should not be interpreted as directly comparable
between leagues.

## 2. Passing Index V2

Passing Index V2 is a weighted composite of four
role-relative percentile metrics:

| Component | Weight |
|---|---:|
| Completed progressive passes per 90 | 40% |
| Progressive passing accuracy | 25% |
| Overall passing accuracy | 15% |
| Total passes per 90 | 20% |

Each component is converted into a percentile rank
within the player's league and broad tactical role,
using:

`pandas.Series.rank(pct=True, method="average") * 100`

The weighted percentiles are summed to produce
Passing Index V2.

Final league rankings use standard competition ranking
(`rank(method="min", ascending=False)`), so tied
scores receive equal ranks and subsequent rank
numbers may be skipped.

## 3. Progressive Passing

Progressive Pass V2 uses a goal-distance reduction
threshold dependent on the pass's starting x-coordinate:

| Starting x-coordinate | Required reduction |
|---|---:|
| x < 40 | 15 units |
| 40 <= x < 80 | 10 units |
| 80 <= x < 102 | 5 units |

Progressive attempts include unsuccessful qualifying
passes. Completed progressive passes require successful
completion.

## 4. Tactical Role Classification

Players are assigned to the broad tactical group in
which they accumulated the largest share of reconstructed
playing minutes:

- Defensive Midfield
- Central Midfield
- Attacking / Wide

Role stability is based on the percentage-point
difference between the two largest broad-role shares:

| Category | Margin |
|---|---|
| Borderline | <= 5 points |
| Close | > 5 to 15 points |
| Moderate | > 15 to 30 points |
| Clear | > 30 points |

Reconstructed playing minutes include stoppage time.
Role stability describes deployment classification,
not statistical confidence.

## 5. Statistical Reliability

Overall and progressive passing accuracy are accompanied
by player-level match-cluster bootstrap intervals.

- Resampling unit: observed player-match
- Bootstrap replicates: 10,000 per player
- Confidence level: 95%
- Interval construction: percentile method
- Random seed: 20261102
- Total player-match observations: 5,511

Intervals describe uncertainty under resampling of
observed matches. They are not confidence intervals
for Passing Index V2 scores or league rankings.

Role stability, sample exposure, and match variability
are reported separately from statistical precision.

No official confidence tiers have been validated.

## 6. Reproducibility Verification

A read-only Day 15 research audit independently
reconstructed the published scoring and ranking layer.

| Verification | Result |
|---|---|
| Passing Index V2 scores | 200/200 reproduced |
| League rankings | 200/200 reproduced |
| Archived research artifacts | 9/9 SHA-256 verified |
| Ranking discrepancies | 0 |

The score reconstruction used the four published
component metrics and the documented role-relative
percentile formula.

This verifies the published scoring and ranking layer.
It does not establish complete reproducibility of
the upstream raw-event processing pipeline.

## 7. Validation Context

The original Day 8 research archive documents an
experimental Hybrid 75/25 model.

Its reported Spearman ranking correlation with the
production Passing Index V2 model was 0.9952.

The experimental model was not adopted as the frozen
production ranking model.

The original research also includes team-cluster
bootstrap analysis of expected-threat relationships,
but these findings do not establish predictive validity.

## 8. Research Limitations

- Passing Index V2 measures passing characteristics,
  not overall player quality.
- Defensive performance is not incorporated.
- Broad role assignments simplify mixed-role deployment.
- Reconstructed minutes include stoppage time.
- Observational passing metrics may reflect tactical,
  team, and selection effects.
- Bootstrap intervals reflect observed-match resampling,
  not future-season predictive accuracy.
- Rankings are descriptive rather than predictive.
- Cross-league score comparisons are unsupported.
- Complete raw-event-to-score reproducibility has
  not yet been independently demonstrated.

## 9. Data Provenance

Research uses StatsBomb open event data.

The original Google Drive research archive contains
match-level event datasets, intermediate research
artifacts, methodology specifications, and validation
outputs.

A Day 10 reproducibility manifest records SHA-256
checksums for nine frozen research artifacts.

This document is a research methodology draft and
has not yet been published to the ScoutIQ repository.
